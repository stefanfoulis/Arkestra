import django.http as http
from django.template import RequestContext
import django.shortcuts as shortcuts
from django.core.exceptions import ViewDoesNotExist
from models import Person, Building, Site, Membership, Entity


from django.contrib.contenttypes.models import ContentType
from links.models import Link

from django.conf import settings

applications = getattr(settings, 'INSTALLED_APPS')

multiple_entity_mode = getattr(settings, "MULTIPLE_ENTITY_MODE", False)
if not multiple_entity_mode and Entity.objects.all():
    default_entity = Entity.objects.get(id = getattr(settings, 'ARKESTRA_BASE_ENTITY'))
else:
    default_entity = None

google_maps_key = getattr(settings, "GOOGLE_MAPS_API_KEY", "")

if 'publications' in applications:
    from publications.models import BibliographicRecord
    from publications.models import Researcher # required for publications

default_template = getattr(settings, 'CMS_DEFAULT_TEMPLATE')

def contacts_and_people(request, slug):
    print "-------- views.contacts_and_people --------"
    # general values needed to set up and construct the page and menus
    entity = Entity.objects.get(slug=slug)
    request.page_path = request.path # for the menu, because next we mess up the path
    request.path = entity.get_website().get_absolute_url()
    template = entity.get_template()
    main_page_body_file = "includes/contacts_and_people.html"

    # meta values - title and meta
    title = "Contact information for %s" % entity
    meta = {
        "description": "Addresses, phone numbers, staff lists and other contact information",
        }

    # content values
    contacts = entity.get_contacts()
    address = entity.get_address()
    email = entity.email
    phone = entity.phone_contacts
    location = entity.precise_location
    access_note = entity.access_note
    roles = entity.get_roles()
    people = entity.get_people()
    people, initials = entity.get_people_and_initials()
    # does the list of role exhaust the list of people too? if so, don't bother showing people separately
    if not set(people) - set([role.person for role in roles]):
        people = []
    return shortcuts.render_to_response(
        "contacts_and_people/entity_information.html", # this is a catch-all template, that then uses includes to bring in extra information
        {
            "entity":entity,
            "pagetitle": entity,
            "entity.website.template": template,
            "main_page_body_file": main_page_body_file,

            "title": title,
            "meta": meta,

            "contacts": contacts,
            "address": address,
            "email": email,
            "phone": phone,
            "location": location,
            "access_note": access_note,
            "roles": roles,
            "people": people,
            "initials_list": initials,
        },
        RequestContext(request),
        )        

def people(request, slug, letter=None):
    """
    Responsible for lists of people
    """
    print "-------- views.people --------"
    # general values - entity, request, template
    entity = Entity.objects.get(slug=slug)
    request.page_path = request.path # for the menu, because next we mess up the path
    request.path = entity.get_website().get_absolute_url()
    template = entity.get_template()
    main_page_body_file = "includes/people_list.html"
    # meta values - title and meta
    meta = {
        "description": "People in %s" % entity,
        }
    title = "%s: people" % entity
    # content values
    people, initials = entity.get_people_and_initials()
    if letter:
        people = entity.get_people(letter)
        title = "%s, people by surname: %s" % (entity, letter.upper())
    return shortcuts.render_to_response(
        "contacts_and_people/entity_information.html",
        {
            "entity":entity,
            "pagetitle": entity,
            "entity.website.template": template,
            "main_page_body_file": main_page_body_file,

            "title": title,
            "meta": meta,

            "people": people,
            "initials_list": initials,
            "letter": letter,
        },
        RequestContext(request),
        )

def publications(request, slug):
    entity = Entity.objects.get(slug=slug)
    request.current_page = entity.website
    return shortcuts.render_to_response(
        "contacts_and_people/publications.html",
        {"entity":entity,},
        RequestContext(request),
    )        

def person(request, slug, active_tab = ""):
    """
    Responsible for the person pages
    """
    print " -------- views.person --------"
    # the straightforward person attributes:            
    person = Person.objects.get(slug=slug)
    access_note = person.access_note
    # attributes that need to be obtained from please_contact:
    contact = person.get_please_contact()
    email = contact.email
    phone = contact.phone_contacts
    if person.please_contact:
        location = None
    else: 
        location = person.precise_location
    # information is based on the Person's most important entity:
    home_role = person.get_role() # could be None
    # if we can't do home_role.entity.get_address() it means that this person has no memberships at all: 
    try:
        address = person.get_address()
        entity = person.get_entity() # used for address information
        template = entity.get_template() 
    except AttributeError: # no memberships, no useful information
        print "no memberships, no useful information"
        address = None
        location = None
        entity = default_entity
        template = default_template
    if default_entity:
        request.current_page = default_entity.get_website()
    else:
        request.current_page = entity.get_website() # for the menu, so it knows where we are
    tabs = []
    if 'publications' in applications:
        try:
            if person.researcher and person.researcher.publishes:
                tabs.extend(("research","publications"))
        except Researcher.DoesNotExist:
            pass
    # meta values - title and meta
    if multiple_entity_mode:
        person_description = str(home_role)
        if person.override_entity:
            person_description = person_description + str(override_entity.entity)
        else:
            person_description = person_description + str(home_role.entity)
    else:
        person_description = str(home_role)
    print person_description
    
    meta = {
        "description": ", ".join([str(person), person_description])
        }
    print meta
    return shortcuts.render_to_response(
        "contacts_and_people/persondetails" + str(active_tab) + ".html",
        {
            "person":person, # personal information
            "home_role": home_role, # entity and position
            "entity": entity,
            "template": template, # from entity
            "address": address, # from entity
            "email": email, # from person or please_contact
            "location": location, # from person, or None 
            "contact": contact, # from person or please_contact
            "phone": phone,
            "access_note": access_note, # from person
            "tabs": tabs,
            "active_tab": active_tab,
            "multiple_entity_mode": multiple_entity_mode,
            "meta": meta,
        },
        RequestContext(request),
        )

def place(request, slug):
    print "place(request, slug):"
    place = Building.objects.get(slug=slug)
    place.row_class="plugin row"
    place.getting_here_div_class = place.access_and_parking_div_class = "column firstcolumn"
    if place.getting_here and place.access_and_parking:
        place.row_class=place.row_class+" columns2"
        place.access_and_parking_div_class = "column lastcolumn"
    else: 
        place.row_class=place.row_class+" columns1"
    if default_entity:
        request.current_page = default_entity.get_website()
    else:
        request.current_page = entity.get_website() # for the menu, so it knows where we are
    return shortcuts.render_to_response(
        "contacts_and_people/place.html",
        {"place":place, 
        "key": google_maps_key,
        "template": default_template,
        },
        RequestContext(request),        )
        
def ajaxGetMembershipForPerson(request):
  #Which person was/is selected
    try:
      person_id = int( request.GET.get("person_id") )
    except ValueError:
      person_id = 0
  #If editing a current displayrole
    try:
      displayrole_id = int( request.GET.get("displayrole_id") )
    except ValueError:
      displayrole_id = 0      
  #If editing a current membership
    try:
      membership_id = int( request.GET.get("membership_id") )
    except ValueError:
      membership_id = 0
  #Server response to AJAX
    response = http.HttpResponse()
  #BLANK option
    response.write ('<option value="">---------</option>')
  #If valid person selected make <option> list of all their existing memberships
    if (person_id > 0 ):
      membership_forperson_list = Membership.objects.filter(person__id = person_id).order_by('entity__name')
      for membership in membership_forperson_list:
        #dont include this membership if it is the one we are editing
        if membership.id != membership_id:
          #add a SELECTED clause if this is the display_role that was previously chosen
            if membership.id == displayrole_id:
              is_selected = " selected "
            else:
              is_selected = ""
          #return an <option> entry for that membership
            response.write('<option ' + is_selected + ' value="' + str(membership.id) + '">' + \
                               str(membership.entity) + ' - ' + str(membership.role) + \
                           '</option>')
  #Done
    return response        