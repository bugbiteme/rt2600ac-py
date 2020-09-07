# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = rt2600ac_py.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging
import json

import synology_srm

from rt2600ac_py import __version__

__author__ = "Leon Levy"
__copyright__ = "Leon Levy"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args=""):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a demonstration of the Synology Router API wrapper")
    parser.add_argument(
        "--version",
        action="version",
        version="rt2600ac-py {ver}".format(ver=__version__))
    #parser.add_argument(
    #    dest="n",
    #    help="n-th Fibonacci number",
    #    type=int,
    #    metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")

    # client connection information
    client = synology_srm.Client(
      host='192.168.1.1',
      port=8001,
      https=True,
      username='admin',
      password="<password>"
    )

    # to get to work without cert
    client.http.disable_https_verify()
    
    #web api base URL
    response = client.http._get_base_url()
    print(response)

    endpoints = client.base.query_info()
    
    # List all the API endpoints available
    # Note: Not all of these are implemented in the pyhon library
    # Will try to call directly with http.call(...) method
    for endpoint, config in endpoints.items():
      print("API endpoint {} (minVersion={}, maxVersion={})".format(
        endpoint,
        config['minVersion'],
        config['maxVersion'],
      ))
    
    # List certificate
    response = client.core.list_certificate()
    print(json.dumps(response, indent=4, sort_keys=True))

    # Get all the hosts, but filter for one specfic known host
    response = client.core.get_network_nsm_device({"hostname": "DESKTOP-6AVJ2SV"})
    print(json.dumps(response, indent=4, sort_keys=True))

    #response = client.core.get_ngfw_traffic("day")
    #print(json.dumps(response, indent=4, sort_keys=True))

    # Test mannually passing in an api endpoint request
    
    # Already supported by synology_srm api
    response = client.http.call(
      endpoint='entry.cgi',
      api='SYNO.Core.DDNS.ExtIP',
      method='list',
      version=1,
    )
    print(json.dumps(response, indent=4, sort_keys=True))
    
    #response = client.http.call(
    #  endpoint='query.cgi',
    #  api='SYNO.API.Info',
    #  method='query',
    #  version=1,
    #)
    #print(json.dumps(response, indent=4, sort_keys=True))

    # This is what the API call looks like from the URL
    #https://192.168.1.1:8001/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all




    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
