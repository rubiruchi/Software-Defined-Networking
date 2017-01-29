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
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
	firstStation= self.addStation('st1')
	#secondStation= self.addStation('st2')
	baseStation= self.addBaseStation("ap1", ssid="new_ssid", channel="10", mode="g")

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( rightSwitch, rightHost )
	self.addLink( rightSwitch, leftSwitch )
	self.addlink(ap1,st1)
        #self.addLink( rightSwitch, firstStation )
	#self.addLink( leftSwitch, secondStation )
	#self.addlink( firstStation, secondStation)	


topos = { 'mytopo': ( lambda: MyTopo() ) }
