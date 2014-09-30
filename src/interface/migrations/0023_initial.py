# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Progress'
        db.create_table(u'interface_progress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('has_general', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_why_us', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_about', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_success_stories', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_services', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_residential_services', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_comercial_services', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_portfolio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_other_services', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_social', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_our_people', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_seo_tools', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_billing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('business_name', self.gf('django.db.models.fields.CharField')(default='Business Name Here', max_length=64, blank=True)),
        ))
        db.send_create_signal(u'interface', ['Progress'])

        # Adding model 'Billing'
        db.create_table(u'interface_billing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.MyUser'])),
            ('stripe_id', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('stripe_id_website_sub', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal(u'interface', ['Billing'])


    def backwards(self, orm):
        # Deleting model 'Progress'
        db.delete_table(u'interface_progress')

        # Deleting model 'Billing'
        db.delete_table(u'interface_billing')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'check_stripe_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'interface.billing': {
            'Meta': {'object_name': 'Billing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'stripe_id_website_sub': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'interface.progress': {
            'Meta': {'object_name': 'Progress'},
            'business_name': ('django.db.models.fields.CharField', [], {'default': "'Business Name Here'", 'max_length': '64', 'blank': 'True'}),
            'has_about': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_billing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_comercial_services': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_general': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_other_services': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_our_people': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_portfolio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_residential_services': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_seo_tools': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_services': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_social': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_success_stories': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_why_us': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.MyUser']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['interface']