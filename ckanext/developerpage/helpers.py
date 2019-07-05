from datetime import datetime
import json
import inspect
import logging
import os

from ckan.common import config, is_flask_request, c, request
from ckan.plugins import toolkit


import platform

log = logging.getLogger(__name__)



def memory_info():
    import psutil
    return dict(psutil.virtual_memory()._asdict())

def get_host_info():
    python_platform = {
            'machine' : platform.machine(),
            'dist' : platform.dist(),
            'py_build' : platform.python_build(),
            'libc' : platform.libc_ver(),
        }
    memory = memory_info()
    python_platform.update(memory)
    return python_platform

def get_ckan_info():
    log.info(config)
    log.info(c)
    return { 'info_item' : 'info_value' }

