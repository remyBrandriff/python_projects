# Custom fully connected mesh topology for Lab06

from mininet.topo import Topo


class MyTopo( Topo ):

    def __init__( self ):

        # initiate the topology
        Topo.__init__( self )

        # add the hosts and switches
        # there should be 9 hosts and 16 switches
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
        sw8 = self.addSwitch('sw8')
        sw9 = self.addSwitch('sw9')
        sw10 = self.addSwitch('sw10')
        sw11 = self.addSwitch('sw11')
        sw12 = self.addSwitch('sw12')
        sw13 = self.addSwitch('sw13')
        sw14 = self.addSwitch('sw14')
        sw15 = self.addSwitch('sw15')
        sw16 = self.addSwitch('sw16')

        # add the links (38 links)
        self.addLink( h1, sw1 )
        self.addLink( h1, sw3 )
        self.addLink( h1, sw4 )

        self.addLink( h2, sw1 )
        self.addLink( h2, sw5 )
        self.addLink( h2, sw2 )

        self.addLink( h3, sw2 )
        self.addLink( h3, sw6 )
        self.addLink( h3, sw7 )

        self.addLink( h4, sw3 )
        self.addLink( h4, sw4 )
        self.addLink( h4, sw8 )
        self.addLink( h4, sw11 )
        self.addLink( h4, sw10 )

        self.addLink( h5, sw8 )
        self.addLink( h5, sw4 )
        self.addLink( h5, sw5 )
        self.addLink( h5, sw6 )
        self.addLink( h5, sw9 )
        self.addLink( h5, sw13 )
        self.addLink( h5, sw12 )
        self.addLink( h5, sw11 )

        self.addLink( h6, sw7 )
        self.addLink( h6, sw6 )
        self.addLink( h6, sw9 )
        self.addLink( h6, sw13 )
        self.addLink( h6, sw14 )

        self.addLink( h7, sw10 )
        self.addLink( h7, sw11 )
        self.addLink( h7, sw15 )

        self.addLink( h8, sw15 )
        self.addLink( h8, sw11 )
        self.addLink( h8, sw12 )
        self.addLink( h8, sw13 )
        self.addLink( h8, sw16 )

        self.addLink( h9, sw16 )
        self.addLink( h9, sw13 )
        self.addLink( h9, sw14 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
