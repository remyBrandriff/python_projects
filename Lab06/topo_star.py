# Custom star + bus topology for Lab06

from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # initiate the topology
        Topo.__init__( self )

        # add the hosts and switches
        # there should be 9 hosts and 7 switches
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
        sw2 = self.addSwitch('sw2')
        sw3 = self.addSwitch('sw3')
        sw4 = self.addSwitch('sw4')
        sw5 = self.addSwitch('sw5')
        sw6 = self.addSwitch('sw6')
        sw7 = self.addSwitch('sw7')

        # add the links (15 links)
        self.addLink( h1, sw1 )
        self.addLink( sw1, h2 )
        self.addLink( h2, sw2 )
        self.addLink( sw2, h3 )
        self.addLink( h3, sw3 )

        self.addLink( h4, sw5 )
        self.addLink( sw5, h5 )
        self.addLink( h5, sw4 )
        self.addLink( sw4, h6 )
        self.addLink( h6, sw3 )

        self.addLink( h7, sw7 )
        self.addLink( sw7, h8 )
        self.addLink( h8, sw6 )
        self.addLink( sw6, h9 )
        self.addLink( h9, sw3 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
