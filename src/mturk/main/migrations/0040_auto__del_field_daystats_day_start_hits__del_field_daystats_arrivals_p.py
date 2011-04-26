# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'DayStats.day_start_hits'
        db.delete_column('main_daystats', 'day_start_hits')

        # Deleting field 'DayStats.arrivals_projects'
        db.delete_column('main_daystats', 'arrivals_projects')

        # Deleting field 'DayStats.arrivals_reward'
        db.delete_column('main_daystats', 'arrivals_reward')

        # Deleting field 'DayStats.day_start_reward'
        db.delete_column('main_daystats', 'day_start_reward')

        # Deleting field 'DayStats.day_end_reward'
        db.delete_column('main_daystats', 'day_end_reward')

        # Deleting field 'DayStats.day_end_hits'
        db.delete_column('main_daystats', 'day_end_hits')

        # Deleting field 'DayStats.day_end_projects'
        db.delete_column('main_daystats', 'day_end_projects')

        # Deleting field 'DayStats.arrivals_hits'
        db.delete_column('main_daystats', 'arrivals_hits')

        # Deleting field 'DayStats.day_start_projects'
        db.delete_column('main_daystats', 'day_start_projects')

        # Adding field 'DayStats.arrivals'
        db.add_column('main_daystats', 'arrivals', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'DayStats.processed'
        db.add_column('main_daystats', 'processed', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'DayStats.day_start_hits'
        db.add_column('main_daystats', 'day_start_hits', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.arrivals_projects'
        db.add_column('main_daystats', 'arrivals_projects', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.arrivals_reward'
        db.add_column('main_daystats', 'arrivals_reward', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.day_start_reward'
        db.add_column('main_daystats', 'day_start_reward', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.day_end_reward'
        db.add_column('main_daystats', 'day_end_reward', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.day_end_hits'
        db.add_column('main_daystats', 'day_end_hits', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.day_end_projects'
        db.add_column('main_daystats', 'day_end_projects', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.arrivals_hits'
        db.add_column('main_daystats', 'arrivals_hits', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'DayStats.day_start_projects'
        db.add_column('main_daystats', 'day_start_projects', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Deleting field 'DayStats.arrivals'
        db.delete_column('main_daystats', 'arrivals')

        # Deleting field 'DayStats.processed'
        db.delete_column('main_daystats', 'processed')


    models = {
        'main.crawl': {
            'Meta': {'object_name': 'Crawl'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'errors': ('mturk.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'groups_available': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'groups_downloaded': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'has_diffs': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'hits_available': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hits_downloaded': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'main.crawlagregates': {
            'Meta': {'object_name': 'CrawlAgregates'},
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Crawl']"}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projects': ('django.db.models.fields.IntegerField', [], {}),
            'reward': ('django.db.models.fields.FloatField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
        'main.daystats': {
            'Meta': {'object_name': 'DayStats'},
            'arrivals': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.hitgroupcontent': {
            'Meta': {'object_name': 'HitGroupContent'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000000'}),
            'first_crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Crawl']", 'null': 'True', 'blank': 'True'}),
            'group_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'group_id_hashed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'max_length': '100000000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'occurrence_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'qualifications': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'requester_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'requester_name': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'reward': ('django.db.models.fields.FloatField', [], {}),
            'time_alloted': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        'main.hitgroupfirstoccurences': {
            'Meta': {'object_name': 'HitGroupFirstOccurences'},
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Crawl']"}),
            'group_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.HitGroupContent']"}),
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'group_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.HitGroupStatus']"}),
            'hits_available': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurrence_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'requester_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'requester_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'reward': ('django.db.models.fields.FloatField', [], {})
        },
        'main.hitgroupstatus': {
            'Meta': {'object_name': 'HitGroupStatus'},
            'crawl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Crawl']"}),
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'hit_expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'hit_group_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.HitGroupContent']"}),
            'hits_available': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inpage_position': ('django.db.models.fields.IntegerField', [], {}),
            'page_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.indexqueue': {
            'Meta': {'object_name': 'IndexQueue'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hitgroupcontent_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requester_id': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'main.requesterprofile': {
            'Meta': {'object_name': 'RequesterProfile'},
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'requester_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'primary_key': 'True'})
        }
    }

    complete_apps = ['main']
