# Custom ring topology for Lab06

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # initiate the topology
        Topo.__init__( self )

        # add the hosts and switches
        # there should be 9 hosts and 9 switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')

        sw1 = self.addSwitch('sw1')

        # add the links
        # there should be 18 links making the ring
        self.addLink( h1, sw1 )
        self.addLink( h2, sw1 )
        self.addLink( h3, sw1 )
        self.addLink( h4, sw1 )
        self.addLink( h5, sw1 )
        self.addLink( h6, sw1 )
        self.addLink( h7, sw1 )
        self.addLink( h8, sw1 )
        self.addLink( h9, sw1 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
