#!/usr/bin/python3

# Copyright {% now 'local', '%Y' %} {{cookiecutter.organization}}
# See LICENSE for details.
# Author: {{cookiecutter.author}} @{{cookiecutter.author_github}} on GitHub


from flask_caching import Cache
from flask_limiter import Limiter	
from flask_limiter.util import get_remote_address


limiter = Limiter(	
	key_func=get_remote_address,	
	default_limits=["1000 per hour"]
) #get_remote_address return the IP address for the current request. If IP adress not found, return 127.0.0.1 (localhost)


cache = Cache(
	config={
		'CACHE_TYPE': 'simple',
		'CACHE_DEFAULT_TIMEOUT': 1
	}
)