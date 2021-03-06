
from south.db import db
from django.db import models
from news_and_events.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'EventType'
        db.create_table('news_and_events_eventtype', (
            ('id', orm['news_and_events.EventType:id']),
            ('event_type', orm['news_and_events.EventType:event_type']),
        ))
        db.send_create_signal('news_and_events', ['EventType'])
        
        # Adding model 'NewsArticle'
        db.create_table('news_and_events_newsarticle', (
            ('id', orm['news_and_events.NewsArticle:id']),
            ('title', orm['news_and_events.NewsArticle:title']),
            ('subtitle', orm['news_and_events.NewsArticle:subtitle']),
            ('short_title', orm['news_and_events.NewsArticle:short_title']),
            ('summary', orm['news_and_events.NewsArticle:summary']),
            ('content', orm['news_and_events.NewsArticle:content']),
            ('hosted_by', orm['news_and_events.NewsArticle:hosted_by']),
            ('slug', orm['news_and_events.NewsArticle:slug']),
            ('date', orm['news_and_events.NewsArticle:date']),
        ))
        db.send_create_signal('news_and_events', ['NewsArticle'])
        
        # Adding model 'Event'
        db.create_table('news_and_events_event', (
            ('id', orm['news_and_events.Event:id']),
            ('title', orm['news_and_events.Event:title']),
            ('subtitle', orm['news_and_events.Event:subtitle']),
            ('short_title', orm['news_and_events.Event:short_title']),
            ('summary', orm['news_and_events.Event:summary']),
            ('content', orm['news_and_events.Event:content']),
            ('hosted_by', orm['news_and_events.Event:hosted_by']),
            ('slug', orm['news_and_events.Event:slug']),
            ('type', orm['news_and_events.Event:type']),
            ('parent', orm['news_and_events.Event:parent']),
            ('series', orm['news_and_events.Event:series']),
            ('child_list_heading', orm['news_and_events.Event:child_list_heading']),
            ('start_date', orm['news_and_events.Event:start_date']),
            ('start_time', orm['news_and_events.Event:start_time']),
            ('end_date', orm['news_and_events.Event:end_date']),
            ('end_time', orm['news_and_events.Event:end_time']),
            ('single_day_event', orm['news_and_events.Event:single_day_event']),
            ('building', orm['news_and_events.Event:building']),
            ('precise_location', orm['news_and_events.Event:precise_location']),
            ('access_note', orm['news_and_events.Event:access_note']),
            ('lft', orm['news_and_events.Event:lft']),
            ('rght', orm['news_and_events.Event:rght']),
            ('tree_id', orm['news_and_events.Event:tree_id']),
            ('level', orm['news_and_events.Event:level']),
        ))
        db.send_create_signal('news_and_events', ['Event'])
        
        # Adding ManyToManyField 'NewsArticle.publish_to'
        db.create_table('news_and_events_newsarticle_publish_to', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('entity', models.ForeignKey(orm['contacts_and_people.Entity'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.organisers'
        db.create_table('news_and_events_event_organisers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'NewsArticle.related_people'
        db.create_table('news_and_events_newsarticle_related_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'NewsArticle.related_pages'
        db.create_table('news_and_events_newsarticle_related_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('page', models.ForeignKey(orm['cms.Page'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.speakers'
        db.create_table('news_and_events_event_speakers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'NewsArticle.enquiries'
        db.create_table('news_and_events_newsarticle_enquiries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.related_people'
        db.create_table('news_and_events_event_related_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'NewsArticle.related_events'
        db.create_table('news_and_events_newsarticle_related_events', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('event', models.ForeignKey(orm.Event, null=False))
        ))
        
        # Adding ManyToManyField 'Event.publish_to'
        db.create_table('news_and_events_event_publish_to', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('entity', models.ForeignKey(orm['contacts_and_people.Entity'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.related_newsarts'
        db.create_table('news_and_events_event_related_newsarts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('newsarticle', models.ForeignKey(orm.NewsArticle, null=False))
        ))
        
        # Adding ManyToManyField 'NewsArticle.related_newsarts'
        db.create_table('news_and_events_newsarticle_related_newsarts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_newsarticle', models.ForeignKey(orm.NewsArticle, null=False)),
            ('to_newsarticle', models.ForeignKey(orm.NewsArticle, null=False))
        ))
        
        # Adding ManyToManyField 'Event.enquiries'
        db.create_table('news_and_events_event_enquiries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.registration_enquiries'
        db.create_table('news_and_events_event_registration_enquiries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('person', models.ForeignKey(orm['contacts_and_people.Person'], null=False))
        ))
        
        # Adding ManyToManyField 'Event.related_events'
        db.create_table('news_and_events_event_related_events', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_event', models.ForeignKey(orm.Event, null=False)),
            ('to_event', models.ForeignKey(orm.Event, null=False))
        ))
        
        # Adding ManyToManyField 'Event.related_pages'
        db.create_table('news_and_events_event_related_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('page', models.ForeignKey(orm['cms.Page'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'EventType'
        db.delete_table('news_and_events_eventtype')
        
        # Deleting model 'NewsArticle'
        db.delete_table('news_and_events_newsarticle')
        
        # Deleting model 'Event'
        db.delete_table('news_and_events_event')
        
        # Dropping ManyToManyField 'NewsArticle.publish_to'
        db.delete_table('news_and_events_newsarticle_publish_to')
        
        # Dropping ManyToManyField 'Event.organisers'
        db.delete_table('news_and_events_event_organisers')
        
        # Dropping ManyToManyField 'NewsArticle.related_people'
        db.delete_table('news_and_events_newsarticle_related_people')
        
        # Dropping ManyToManyField 'NewsArticle.related_pages'
        db.delete_table('news_and_events_newsarticle_related_pages')
        
        # Dropping ManyToManyField 'Event.speakers'
        db.delete_table('news_and_events_event_speakers')
        
        # Dropping ManyToManyField 'NewsArticle.enquiries'
        db.delete_table('news_and_events_newsarticle_enquiries')
        
        # Dropping ManyToManyField 'Event.related_people'
        db.delete_table('news_and_events_event_related_people')
        
        # Dropping ManyToManyField 'NewsArticle.related_events'
        db.delete_table('news_and_events_newsarticle_related_events')
        
        # Dropping ManyToManyField 'Event.publish_to'
        db.delete_table('news_and_events_event_publish_to')
        
        # Dropping ManyToManyField 'Event.related_newsarts'
        db.delete_table('news_and_events_event_related_newsarts')
        
        # Dropping ManyToManyField 'NewsArticle.related_newsarts'
        db.delete_table('news_and_events_newsarticle_related_newsarts')
        
        # Dropping ManyToManyField 'Event.enquiries'
        db.delete_table('news_and_events_event_enquiries')
        
        # Dropping ManyToManyField 'Event.registration_enquiries'
        db.delete_table('news_and_events_event_registration_enquiries')
        
        # Dropping ManyToManyField 'Event.related_events'
        db.delete_table('news_and_events_event_related_events')
        
        # Dropping ManyToManyField 'Event.related_pages'
        db.delete_table('news_and_events_event_related_pages')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.page': {
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'menu_login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'page_flags': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'contacts_and_people.building': {
            'additional_street_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'contacts_and_people.entity': {
            'abstract_entity': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'access_note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'auto_contacts_page': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_news_page': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_vacancies_page': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Building']", 'null': 'True', 'blank': 'True'}),
            'contacts_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'Contacts & people'", 'max_length': '50'}),
            'display_parent': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'entitylite_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts_and_people.EntityLite']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']", 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'news_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'News & events'", 'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['contacts_and_people.Entity']"}),
            'phone_contacts': ('django.contrib.contenttypes.generic.GenericRelation', [], {'to': "orm['contacts_and_people.PhoneContact']"}),
            'precise_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'vacancies_page_menu_title': ('django.db.models.fields.CharField', [], {'default': "'Vacancies & studentships'", 'max_length': '50'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'entity'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"})
        },
        'contacts_and_people.entitylite': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contacts_and_people.person': {
            'access_note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'data_feed_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'entities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Entity']", 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']", 'null': 'True', 'blank': 'True'}),
            'institutional_username': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'override_entity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people_override'", 'null': 'True', 'to': "orm['contacts_and_people.Entity']"}),
            'personlite_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contacts_and_people.PersonLite']", 'unique': 'True', 'primary_key': 'True'}),
            'phone_contacts': ('django.contrib.contenttypes.generic.GenericRelation', [], {'to': "orm['contacts_and_people.PhoneContact']"}),
            'please_contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_for'", 'null': 'True', 'to': "orm['contacts_and_people.Person']"}),
            'precise_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'staff_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_user'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'contacts_and_people.personlite': {
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Title']", 'to_field': "'abbreviation'", 'null': 'True', 'blank': 'True'})
        },
        'contacts_and_people.phonecontact': {
            'area_code': ('django.db.models.fields.CharField', [], {'default': "'029'", 'max_length': '5'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'default': "'44'", 'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_extension': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'contacts_and_people.site': {
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']", 'null': 'True', 'blank': 'True'}),
            'post_town': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'contacts_and_people.title': {
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'image_filer.folder': {
            'Meta': {'unique_together': "(('parent', 'name'),)"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'image_filer.image': {
            '_height_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_use_for_print': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_private_use': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_research': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_teaching': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_web': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_of_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'image_files'", 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_images'", 'null': 'True', 'to': "orm['auth.User']"}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'usage_restriction_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'news_and_events.event': {
            'access_note': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts_and_people.Building']", 'null': 'True', 'blank': 'True'}),
            'child_list_heading': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'enquiries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'hosted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event_hosted_events'", 'null': 'True', 'to': "orm['contacts_and_people.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'organisers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['news_and_events.Event']"}),
            'precise_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Entity']", 'null': 'True', 'blank': 'True'}),
            'registration_enquiries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'related_events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['news_and_events.Event']", 'null': 'True', 'blank': 'True'}),
            'related_newsarts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['news_and_events.NewsArticle']", 'null': 'True', 'blank': 'True'}),
            'related_pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'related_people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'series': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'single_day_event': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['news_and_events.EventType']"})
        },
        'news_and_events.eventtype': {
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'news_and_events.newsarticle': {
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'enquiries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'hosted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'newsarticle_hosted_events'", 'null': 'True', 'to': "orm['contacts_and_people.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_to': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Entity']", 'null': 'True', 'blank': 'True'}),
            'related_events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['news_and_events.Event']", 'null': 'True', 'blank': 'True'}),
            'related_newsarts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['news_and_events.NewsArticle']", 'null': 'True', 'blank': 'True'}),
            'related_pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'related_people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts_and_people.Person']", 'null': 'True', 'blank': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['news_and_events']
