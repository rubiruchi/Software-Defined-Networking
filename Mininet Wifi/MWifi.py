#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import  Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.topo import Topo

def topology():
	"Create a network."
	net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )
   	print "*** Creating nodes"
   	sta1 = net.addStation( 'sta1', ip="192.168.0.1" )
    	sta2 = net.addStation( 'sta2', ip="192.168.0.2" )
    	ap1 = net.addBaseStation( 'ap1', ssid="ssid_1", mode="g", channel="7" )
	ap2 = net.addBaseStation( 'ap2', ssid="ssid_2", mode="g", channel="7" )
	    
    	s1 = net.addSwitch( 's1', ip="192.168.0.35")
    	s2 = net.addSwitch( 's2', ip="192.168.0.36")
    	s3 = net.addSwitch( 's3', ip="192.168.0.37")
    	s4 = net.addSwitch( 's4', ip="192.168.0.38")
    
    	h1 = net.addHost( 'h1', ip="192.168.0.3" )
    	h2 = net.addHost( 'h2', ip="192.168.0.4" )
    	h3 = net.addHost( 'h3', ip="192.168.0.5" )
    	h4 = net.addHost( 'h4', ip="192.168.0.6" )
    	h5 = net.addHost( 'h5', ip="192.168.0.7" )
    	h6 = net.addHost( 'h6', ip="192.168.0.8" )
    	h7 = net.addHost( 'h7', ip="192.168.0.9" )
    	h8 = net.addHost( 'h8', ip="192.168.0.10" )
    	h9 = net.addHost( 'h9', ip="192.168.0.11" )
    	h10 = net.addHost( 'h10', ip="192.168.0.12" )
    	h11 = net.addHost( 'h11', ip="192.168.0.13" )
    	h12 = net.addHost( 'h12', ip="192.168.0.14" )
    	h13 = net.addHost( 'h13', ip="192.168.0.15" )
    	h14 = net.addHost( 'h14', ip="192.168.0.16" )
    	h15 = net.addHost( 'h15', ip="192.168.0.17" )
    	h16 = net.addHost( 'h16', ip="192.168.0.18" )
    	h17 = net.addHost( 'h17', ip="192.168.0.19" )
    	h18 = net.addHost( 'h18', ip="192.168.0.20" )
    	h19 = net.addHost( 'h19', ip="192.168.0.21" )
    	h20 = net.addHost( 'h20', ip="192.168.0.22" )
    	h21 = net.addHost( 'h21', ip="192.168.0.23" )
    	h22 = net.addHost( 'h22', ip="192.168.0.24" )
    	h23 = net.addHost( 'h23', ip="192.168.0.25" )
    	h24 = net.addHost( 'h24', ip="192.168.0.26" )
    	h25 = net.addHost( 'h25', ip="192.168.0.27" )
    	h26 = net.addHost( 'h26', ip="192.168.0.28" )
    	h27 = net.addHost( 'h27', ip="192.168.0.29" )
    	h28 = net.addHost( 'h28', ip="192.168.0.30" )
    	h29 = net.addHost( 'h29', ip="192.168.0.31" )
    	h30 = net.addHost( 'h30', ip="192.168.0.32" )
    	h31 = net.addHost( 'h31', ip="192.168.0.33" )
    	h32 = net.addHost( 'h32', ip="192.168.0.34" )
    
    	c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633 )

    	print "*** Adding Link"
    	net.addLink(sta1, ap1)
    	net.addLink(sta2, ap2)    
	net.addLink(ap1, ap2)
    
    	net.addLink(s1,ap1)
    	net.addLink(s2,ap1)
    	net.addLink(s3,ap2)
    	net.addLink(s4,ap2)
    	
    	net.addLink(s1,h1)
    	net.addLink(s1,h2)
    	net.addLink(s1,h3)
    	net.addLink(s1,h4)
    	net.addLink(s1,h5)
    	net.addLink(s1,h6)
    	net.addLink(s1,h7)
    	net.addLink(s1,h8)   
    	
    	net.addLink(s2,h9)
    	net.addLink(s2,h10)
    	net.addLink(s2,h11)
    	net.addLink(s2,h12)
    	net.addLink(s2,h13)
    	net.addLink(s2,h14)
    	net.addLink(s2,h15)
    	net.addLink(s2,h16)
    	
    	net.addLink(s3,h17)
    	net.addLink(s3,h18)
    	net.addLink(s3,h19)
    	net.addLink(s3,h20)
    	net.addLink(s3,h21)
    	net.addLink(s3,h22)
    	net.addLink(s3,h23)
    	net.addLink(s3,h24)
    	
    	net.addLink(s4,h25)
    	net.addLink(s4,h26)
    	net.addLink(s4,h27)
    	net.addLink(s4,h28)
    	net.addLink(s4,h29)
    	net.addLink(s4,h30)
    	net.addLink(s4,h31)
    	net.addLink(s4,h32)    
    	print "*** Starting network"
    	net.build()
    	c0.start()
    	ap1.start( [c0] )
    	ap2.start( [c0] )
	s1.start( [c0] )
	s2.start( [c0] )
	s3.start( [c0] )    	
	s4.start( [c0] )	
	
	print "*** Running CLI"
    	CLI( net )
    	print "*** Stopping network"
    	net.stop()

if __name__ == '__main__':
    	setLogLevel( 'info' )
    	topology()

