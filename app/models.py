import datetime
from app import db

PLATFORMS = ('Windows', 'Linux', 'All', 'macOS')
STATUSOPTIONS = ('Processed', 'Open', 'Processing')
TYPEOPTIONS = ('Manual', 'Mitre', 'Actor')


class Credentials(db.Document):
    beacon_id = db.StringField(max_length=50, required=False)
    beacon_hostname = db.StringField(max_length=50, required=False)
    source_command = db.StringField(max_length=50, required=False)
    username = db.StringField(unique_with=['key', 'type'])
    key = db.StringField()
    type = db.StringField()


class Targets(db.Document):
    source_beacon = db.StringField(max_length=50, required=False)
    destination_ip = db.StringField(max_length=50)
    ports = db.DictField()
    hostname = db.StringField()


class Beacons(db.Document):
    beacon_id = db.StringField(max_length=150, required=True, unique=True)
    timestamp =  db.DateTimeField(default=datetime.datetime.now)
    platform = db.StringField(max_length=25, required=True)
    username = db.StringField(max_length=100, required=True)
    remote_ip = db.StringField(max_length=39, required=True)
    hostname = db.StringField(max_length=250, required=True)
    working_dir = db.StringField(max_length=800, required=False)
    timer = db.IntField(default=300)
    data = db.DictField()


class BeaconKeylogger(db.Document):
    beacon_id = db.StringField(max_length=150, required=True, unique=True)
    keyLoggerData = db.ListField()


class BeaconHistory(db.Document):
    beacon_id = db.StringField(max_length=150, required=True)
    platform = db.StringField(max_length=25, required=True)
    timestamp = db.DateTimeField(default=datetime.datetime.now)
    remote_ip = db.StringField(max_length=15, required=True)
    hostname = db.StringField(max_length=250, required=True)
    username = db.StringField(max_length=100, required=True)
    working_dir = db.StringField(max_length=400)
    timer = db.IntField()
    data = db.DictField()

    meta = {
        'ordering': ['-timestamp']
    }


class TaskCommands(db.EmbeddedDocument):
    reference = db.StringField(max_length=100, required=False, default=None)
    type = db.StringField(max_length=50, required=True, choices=TYPEOPTIONS)
    name = db.StringField(max_length=150, required=True)
    input = db.StringField(max_length=900, required=False)
    sleep = db.IntField(default=0)


class Tasks(db.Document):
    name = db.StringField(max_length=150, required=True)
    beacon_id = db.StringField(max_length=150, required=True)
    start_date = db.DateTimeField(default=datetime.datetime.now())
    task_status = db.StringField(default="Open", choices=STATUSOPTIONS)
    commands = db.EmbeddedDocumentListField('TaskCommands', required=True)
    meta = {
        'ordering': ['-start_date']
    }


class StartupTasks(db.Document):
    name = db.StringField(max_length=150, required=True, unique=True)
    platform = db.StringField(max_length=150, required=True)
    commands = db.EmbeddedDocumentListField('TaskCommands', required=True)


class TaskResults(db.Document):
    beacon_id = db.StringField(max_length=150, required=True)
    task_id = db.ReferenceField('Tasks', required=True)
    command = db.StringField(max_length=100, required=True) 
    type = db.StringField(max_length=50, required=True)
    input = db.StringField(max_length=900, required=True)
    end_date = db.DateTimeField(default=datetime.datetime.now)
    output = db.FileField()
    meta = {
        'ordering': ['-end_date'],
    }


class Commands(db.Document):
    name = db.StringField(max_length=100, required=True, unique=True)
    reference = db.StringField(max_length=100, required=False, default=None)
    type = db.StringField(max_length=20, required=True, choices=TYPEOPTIONS)
    platform = db.ListField(db.StringField(max_length=50, default="all"))

