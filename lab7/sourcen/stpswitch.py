from mininet.node import OVSSwitch


class OVSSwitchSTP(OVSSwitch):
    prio = 1000

    def start(self, *args, **kwargs):
        OVSSwitch.start(self, *args, **kwargs)
        OVSSwitchSTP.prio += 1
        self.cmd('ovs-vsctl set-fail-mode', self, 'standalone')
        self.cmd('ovs-vsctl set-controller', self)
        self.cmd('ovs-vsctl set Bridge', self,
                  'stp_enable=true',
                  'other_config:stp-priority=%d' % OVSSwitchSTP.prio)

switches = {'ovs-stp': OVSSwitchSTP}
