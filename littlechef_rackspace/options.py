from optparse import OptionParser

parser = OptionParser()
parser.add_option("-I", "--image", dest="image",
                  help="Image ID or name")
parser.add_option("-f", "--flavor", dest="flavor",
                  help="Flavor ID")
parser.add_option("-A", "--username", dest="username",
                  help="Rackspace Username")
parser.add_option("-N", "--node-name", dest="nodename",
                  help="Node name")
parser.add_option("-K", "--key", dest="apikey",
                  help="Rackspace API Key")
parser.add_option("-v", "--version", type="int", dest="version",
                  default=2, help="API Version (defaults to OpenStack v2)")
parser.add_option("-R", "--region", dest="region", default="",
                  help="Region for provisioning (required for OpenStack)")