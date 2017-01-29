#!/usr/bin/python

 

from mininet.net import Mininet

from mininet.node import  Controller, RemoteController, OVSKernelSwitch

from mininet.cli import CLI

from mininet.log import setLogLevel

from mininet.link import TCLink

 

def topology():

    "Create a network."

    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

 

    print "*** Creating nodes"

    sta1 = net.addStation( 'sta1', ip="192.168.0.1" )

    sta2 = net.addStation( 'sta2', ip="192.168.0.2" )

    h1 = net.addHost( 'h1', ip="192.168.0.3" )

    ap1 = net.addBaseStation( 'ap1', ssid="ssid_1", mode="g", channel="1" )

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

 

    print "*** Adding Link"

    net.addLink(h1,ap1)

    net.addLink(sta1, ap1)

    net.addLink(sta2, ap1)

 

    print "*** Starting network"

    net.build()

    c0.start()

    ap1.start( [c0] )

   

    print "*** Running CLI"

    CLI( net )

    print "*** Stopping network"

    net.stop()

 

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()
