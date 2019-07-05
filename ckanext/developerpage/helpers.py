from datetime import datetime
import json
import inspect
import logging
import os

from ckan.common import config, is_flask_request, c, request
from ckan.plugins import toolkit
from ckan.logic.action.get import status_show

import ckan.model as model
import ckan.logic as logic

from ckan.common import g, config, _



import platform

log = logging.getLogger(__name__)


def memory_info():
    import psutil
    return dict(psutil.virtual_memory()._asdict())

def average_load():
    import psutil
    return psutil.getloadavg()

def get_host_info():
    python_platform = {
            'machine_architecture' : platform.machine(),
            'python_build' : platform.python_build(),
        }
    memory = memory_info()
    load = average_load()
    python_platform.update(memory)
    python_platform.update({'load_average' : load})
    return python_platform

def get_ckan_info():
    context = {
            u'model': model,
            u'user': g.user,
            u'auth_user_obj': g.userobj}
    return status_show(context, data_dict={})

