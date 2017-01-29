"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
	host4 = self.addHost( 'h4' )
	host5 = self.addHost( 'h5' )
	host6 = self.addHost( 'h6' )
	host7 = self.addHost( 'h7' )
	host8 = self.addHost( 'h8' )
	host9 = self.addHost( 'h9' )
	host10 = self.addHost( 'h10' )
	host11 = self.addHost( 'h11' )
	host12 = self.addHost( 'h12' )
	host13 = self.addHost( 'h13' )
	host14 = self.addHost( 'h14' )
	host15 = self.addHost( 'h15' )
	host16 = self.addHost( 'h16' )
	host17 = self.addHost( 'h17' )
	host18 = self.addHost( 'h18' )
	host19 = self.addHost( 'h19' )
	host20 = self.addHost( 'h20' )
	host21 = self.addHost( 'h21' )
	host22 = self.addHost( 'h22' )
	host23 = self.addHost( 'h23' )
	host24 = self.addHost( 'h24' )
	host25 = self.addHost( 'h25' )
	host26 = self.addHost( 'h26' )
	host27 = self.addHost( 'h27' )
	host28 = self.addHost( 'h28' )
	host29 = self.addHost( 'h29' )
	host30 = self.addHost( 'h30' )
	host31 = self.addHost( 'h31' )
	host32 = self.addHost( 'h32' )
	switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
	switch4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( switch1, switch2 )
	self.addLink( switch2, switch3 )
	self.addLink( switch3, switch4 )
	self.addLink( switch1, host1 )
        self.addLink( switch1, host2 )
        self.addLink( switch1, host3 )
	self.addLink( switch1, host4 )
	self.addLink( switch1, host5 )
	self.addLink( switch1, host6 )
	self.addLink( switch1, host7 )
	self.addLink( switch1, host8 )
	self.addLink( switch2, host9 )
	self.addLink( switch2, host10 )
	self.addLink( switch2, host11 )
	self.addLink( switch2, host12 )
	self.addLink( switch2, host13 )
	self.addLink( switch2, host14 )
	self.addLink( switch2, host15 )
	self.addLink( switch2, host16 )
	self.addLink( switch3, host17 )
	self.addLink( switch3, host18 )
	self.addLink( switch3, host19 )
	self.addLink( switch3, host20 )
	self.addLink( switch3, host21 )
	self.addLink( switch3, host22 )
	self.addLink( switch3, host23 )
	self.addLink( switch3, host24 )
	self.addLink( switch4, host25 )
	self.addLink( switch4, host26 )
	self.addLink( switch4, host27 )
	self.addLink( switch4, host28 )
	self.addLink( switch4, host29 )
	self.addLink( switch4, host30 )
	self.addLink( switch4, host31 )
	self.addLink( switch4, host32 )
topos = { 'mytopo': ( lambda: MyTopo() ) }
