#!/usr/bin/env python2.7
"""clos-network.py
Usage:
  clos-network.py <spines> <leafs>
  clos-network.py -h | --help
  clos-network.py  --version
Options:
  -h --help             show this screen.
  --version             show version.
"""

from docopt import docopt
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSController
from ovsstp import OVSSwitchSTP


class ClosNetwork(Topo):

    "Members"
    spineList = []

    def __init__(self, leafs=1, spines=1, **opts):
        super(ClosNetwork, self).__init__(**opts)

        "Create spines"
        for switch_number in range(spines):
            spineSwitch = self.addSwitch("ss%s" % (switch_number + 1))
            self.spineList.append(spineSwitch)

        "Create leafs"
        for switch_number in range(leafs):
            leafSwitch = self.addSwitch("ls%s" % (switch_number + 1))

            "add one host to each leaf"
            host = self.addHost("h%s" % (switch_number + 1))
            self.addLink(host, leafSwitch)

            "Connect with each spine"
            for i in range(len(self.spineList)):
                self.addLink(self.spineList[i], leafSwitch)


def main():
    arguments = docopt(__doc__, version="clos-network.py 1")

    topo = ClosNetwork(
        leafs=int(arguments["<leafs>"]),
        spines=int(arguments["<spines>"])
    )

    net = Mininet(topo=topo, controller=OVSController, switch=OVSSwitchSTP)
    net.start()

    print "Dumping Host Connections:"
    dumpNodeConnections(net.hosts)

    print "Testing network connectivity"
    # net.pingAll()

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
