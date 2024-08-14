############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#
############

def get_value(data, key, default, lookup=None, mapper=None):

# Finds the value from data associated with key, or default if the
# key isn't present.
# If a lookup enum is provided, this value is then transformed to its
# enum value.
# If a mapper function is provided, this value is then transformed
# by applying mapper to it.

    return_value = data[key] #Poor Error handling to avoid KeyError when the key is not in the dictionary data.get(key, default) should be used
    if return_value is None or return_value == "":
        return_value = default
    if lookup:
        return_value = lookup[return_value] #Poor Error handling to avoid KeyError when the key is not in the lookup lookup.get(return_value, return_value) should be used if the return_value is not found as a key keep the same return_value
    if mapper:
        return_value = mapper(return_value) #Poor Error handling to avoid KeyError or other errors that may arrise in the mapper we should use try except
    return return_value

def ftp_file_prefix(namespace):
# Given a namespace string with dot-separated tokens, returns the
# string with
# the final token replaced by 'ftp'.
# Example: a.b.c => a.b.ftp
    return ".".join(namespace.split(".")[:-1]) + '.ftp' #Empty namespace, namespace with several dots(for example token name includes dots) near each other or single namepace token cases need to be treated separately to achieve desired output 

def string_to_bool(string):
# Returns True if the given string is 'true' case-insensitive,
# False if it is
# 'false' case-insensitive.
# Raises ValueError for any other input.
    # We should make sure that the passed argument is truly a string and raise an informative error otherwise
    # Although not significant but string.lower() can be kept as a variable not to be called twice
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')

def config_from_dict(dict):
# Given a dict representing a row from a namespaces csv file,
# returns a DAG configuration as a pair whose first element is the
# DAG name
# and whose second element is a dict describing the DAG's properties
    namespace = dict['Namespace'] #dict shouldn't be used as a variable name its a python special word and KeyError needs to be handled
    return (dict['Airflow DAG'], #KeyError needs to be handled
            {"earliest_available_delta_days": 0,
            "lif_encoding": 'json',
            "earliest_available_time":
            get_value(dict, 'Available Start Time', '07:00'),
            "latest_available_time": get_value(dict, 'Available End Time', '08:00'),# Function get_value may raise an error so we should use try except
            "require_schema_match": get_value(dict, 'Requires Schema Match', 'True',
            mapper=string_to_bool),# Function string_to_bool may raise an error so we should use try except
            "schedule_interval":get_value(dict, 'Schedule', '1 7 * * * '),
            "delta_days": get_value(dict, 'Delta Days', 'DAY_BEFORE', lookup=DeltaDays),
            "ftp_file_wildcard": get_value(dict, 'File Naming Pattern', None),
            "ftp_file_prefix": get_value(dict, 'FTP File Prefix', ftp_file_prefix(namespace)),#We shouldn't pass a function directly should have called it before and passed the returned value here
            "namespace": namespace
}
)