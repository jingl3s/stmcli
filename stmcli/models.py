import peewee

# db connection to be initialized and used around the system
db = None

# max number of inserts that can be done in a single bulk
SQLITE_MAX_VARIABLE_NUMBER = 2 ** 16


class Agency(peewee.Model):
    agency_id = peewee.FixedCharField(
        max_length=3, null=False, primary_key=True)
    agency_name = peewee.CharField(max_length=40, null=False)
    agency_url = peewee.CharField(max_length=60, null=False)
    agency_timezone = peewee.CharField(max_length=20, null=False)

    agency_lang = peewee.CharField(max_length=10, null=True)
    agency_phone = peewee.CharField(max_length=20, null=True)
    agency_fare_url = peewee.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'agency'


class Stop(peewee.Model):
    stop_id = peewee.CharField(primary_key=True)
    stop_code = peewee.CharField()
    stop_name = peewee.CharField(max_length=50, null=False)

    stop_lat = peewee.CharField(null=False)
    stop_lon = peewee.CharField(null=True)
    stop_url = peewee.CharField(max_length=60)
    location_type = peewee.CharField(max_length=60)
    parent_station = peewee.CharField()
    wheelchair_boarding = peewee.CharField(null=True)

    class Meta:
        db_table = 'stops'


class Route(peewee.Model):
    route_id = peewee.CharField(primary_key=True)
    agency_id = peewee.ForeignKeyField(Agency)

    route_short_name = peewee.CharField(max_length=10, null=False)
    route_long_name = peewee.CharField(max_length=40, null=False)
    route_type = peewee.CharField(max_length=10, null=False)
    route_url = peewee.TextField()
    route_color = peewee.CharField(max_length=6)
    route_text_color = peewee.CharField(max_length=6)
    route_desc = peewee.CharField(max_length=100, null=True)
    route_desc_detail = peewee.TextField(null=True)

    class Meta:
        db_table = 'routes'


class Trip(peewee.Model):
    id = peewee.PrimaryKeyField()
    route_id = peewee.ForeignKeyField(Route)
    service_id = peewee.CharField(null=False)
    trip_id = peewee.CharField(max_length=20, null=False)

    trip_headsign = peewee.CharField(max_length=50)
    direction_id = peewee.CharField()
    shape_id = peewee.CharField(max_length=40)
    wheelchair_accessible = peewee.CharField()
    route_pattern_id = peewee.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'trips'


class StopTime(peewee.Model):
    trip_id = peewee.ForeignKeyField(Trip, null=False)
    arrival_time = peewee.CharField(max_length=8, null=False)
    departure_time = peewee.CharField(max_length=8, null=False)
    stop_id = peewee.ForeignKeyField(Stop, null=False)
    stop_sequence = peewee.CharField(null=False)
    pickup_type = peewee.BooleanField(null=True)

    class Meta:
        db_table = 'stop_times'


class CalendarDate(peewee.Model):
    calendar_id = peewee.PrimaryKeyField()
    service_id = peewee.CharField(null=False)
    date = peewee.DateField(null=False)
    exception_type = peewee.CharField(null=False)

    class Meta:
        db_table = 'calendar_dates'


class Calendar(peewee.Model):
    calendar_id = peewee.PrimaryKeyField()
    service_id = peewee.CharField(null=False)
    monday = peewee.CharField(null=False)
    tuesday = peewee.CharField(null=False)
    wednesday = peewee.CharField(null=False)
    thursday = peewee.CharField(null=False)
    friday = peewee.CharField(null=False)
    saturday = peewee.CharField(null=False)
    sunday = peewee.CharField(null=False)
    start_date = peewee.DateField(null=False)
    end_date = peewee.DateField(null=False)

    class Meta:
        db_table = 'calendar'


class Shape(peewee.Model):
    shape_id = peewee.CharField(max_length=40, null=False)
    shape_pt_lat = peewee.CharField(null=False)
    shape_pt_lon = peewee.CharField(null=False)
    shape_pt_sequence = peewee.IntegerField(null=False)
    shape_dist_traveled = peewee.CharField(null=True)
    route_pattern_id = peewee.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'shapes'


class Translation(peewee.Model):
    table_name = peewee.CharField(max_length=40, null=False)
    field_name = peewee.CharField(max_length=40, null=False)
    language = peewee.CharField(max_length=10, null=False)
    translation = peewee.TextField(null=False)
    record_id = peewee.CharField(max_length=40, null=True)
    record_sub_id = peewee.CharField(max_length=40, null=True)
    field_value = peewee.TextField(null=True)

    class Meta:
        db_table = 'translations'
