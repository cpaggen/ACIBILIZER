requiredParamsMap = {'aci_fabric_pod_policy_group': ['name*',
  'date_time_policy',
  'isis_policy',
  'coop_group_policy',
  'bgp_rr_policy',
  'management_access_policy',
  'snmp_policy',
  'macsec_policy',
  'name_alias',
  'state'],
 'aci_esg_contract_master': ['tenant*',
  'ap*',
  'esg*',
  'contract_master_ap*',
  'contract_master_esg*',
  'state',
  'name_alias'],
 'aci_l3out_floating_svi': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id*',
  'node_id*',
  'address*',
  'link_local_address',
  'mac_address',
  'mtu',
  'ipv6_dad',
  'mode',
  'encap*',
  'encap_scope',
  'auto_state',
  'external_bridge_group_profile'],
 'aci_l3out_bgp_peer': ['tenant*',
  'l3out*',
  'description',
  'node_profile*',
  'interface_profile',
  'state',
  'pod_id',
  'node_id',
  'path_ep',
  'peer_ip*',
  'remote_asn',
  'bgp_controls'],
 'aci_bgp_timers_policy': ['tenant*',
  'bgp_timers_policy*',
  'graceful_restart_controls',
  'hold_interval',
  'keepalive_interval',
  'max_as_limit',
  'stale_interval',
  'description',
  'state',
  'name_alias'],
 'aci_l2out': ['bd*',
  'l2out*',
  'domain*',
  'vlan*',
  'description',
  'state',
  'tenant*',
  'name_alias'],
 'aci_l3out_hsrp_group': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'hsrp_interface_group*',
  'group_id',
  'ip',
  'mac',
  'group_name',
  'description',
  'group_type',
  'ip_obtain_mode',
  'group_policy',
  'state'],
 'aci_subject_label': ['tenant*',
  'l2out',
  'l3out',
  'external_epg',
  'contract',
  'subject',
  'ap',
  'epg',
  'esg',
  'complement',
  'description',
  'subject_label*',
  'subject_label_type',
  'tag',
  'state',
  'name_alias'],
 'aci_interface_policy_bfd': ['name*',
  'description',
  'admin_state',
  'detection_multiplier',
  'min_transmit_interval',
  'min_receive_interval',
  'state',
  'tenant*'],
 'aci_vlan_pool': ['pool*',
  'description',
  'pool_allocation_mode',
  'state',
  'name_alias'],
 'aci_domain_to_encap_pool': ['domain_type*',
  'pool_type*',
  'domain*',
  'pool*',
  'pool_allocation_mode',
  'state',
  'vm_provider'],
 'aci_tenant_span_src_group_to_dst_group': ['tenant*',
  'dst_group*',
  'src_group*',
  'description',
  'state',
  'name_alias'],
 'aci_vmm_vswitch_policy': ['port_channel_policy',
  'lldp_policy',
  'cdp_policy',
  'mtu_policy',
  'stp_policy',
  'enhanced_lag',
  'netflow_exporter',
  'domain*',
  'state',
  'vm_provider*'],
 'aci_access_spine_interface_profile_to_spine_switch_profile': ['switch_profile*'],
 'aci_fabric_pod': ['description',
  'state',
  'name_alias',
  'pod_id*',
  'pod_type',
  'tep_pool'],
 'aci_fabric_switch_policy_group': ['name*',
  'switch_type',
  'monitoring_policy',
  'tech_support_export_policy',
  'core_export_policy',
  'inventory_policy',
  'power_redundancy_policy',
  'twamp_server_policy',
  'twamp_responder_policy',
  'node_control_policy',
  'analytics_cluster',
  'analytics_name',
  'description',
  'state'],
 'aci_l3out_logical_interface_profile_ospf_policy': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'ospf_policy*',
  'ospf_auth_type',
  'ospf_auth_key',
  'state'],
 'aci_system_banner': ['description',
  'gui_alias',
  'controller_banner',
  'switch_banner',
  'application_banner',
  'severity',
  'gui_banner',
  'name_alias',
  'state'],
 'aci_contract_export': ['name*',
  'destination_tenant*',
  'description',
  'tenant*',
  'contract*',
  'state'],
 'aci_domain_to_vlan_pool': ['domain_type*',
  'domain*',
  'pool*',
  'pool_allocation_mode',
  'state',
  'vm_provider'],
 'aci_l3out_hsrp_interface_profile': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'hsrp_policy',
  'version',
  'state'],
 'aci_l3out_extsubnet': ['tenant',
  'l3out',
  'extepg',
  'network*',
  'description',
  'subnet_name',
  'scope',
  'aggregate',
  'state',
  'name_alias'],
 'aci_key_policy': ['tenant*',
  'keychain_policy*',
  'id*',
  'start_time',
  'end_time',
  'pre_shared_key',
  'description',
  'state'],
 'aci_l3out_logical_interface_profile': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'nd_policy',
  'egress_dpp_policy',
  'ingress_dpp_policy',
  'qos_priority',
  'qos_custom_policy',
  'pim_v4_interface_profile',
  'pim_v6_interface_profile',
  'igmp_interface_profile',
  'state',
  'description'],
 'aci_l3out_static_routes': ['tenant*',
  'l3out*',
  'logical_node*',
  'pod_id*',
  'node_id*',
  'prefix*',
  'track_policy',
  'preference',
  'bfd',
  'description',
  'state',
  'name_alias'],
 'aci_interface_policy_pim': ['tenant*',
  'pim*',
  'description',
  'authentication_key',
  'authentication_type',
  'control_state',
  'designated_router_delay',
  'designated_router_priority',
  'hello_interval',
  'join_prune_interval',
  'inbound_join_prune_filter_policy',
  'outbound_join_prune_filter_policy',
  'neighbor_filter_policy',
  'state',
  'name_alias'],
 'aci_epg': ['epg*',
  'bd',
  'ap*',
  'tenant*',
  'description',
  'priority',
  'intra_epg_isolation',
  'fwd_control',
  'preferred_group',
  'state',
  'name_alias',
  'monitoring_policy',
  'custom_qos_policy',
  'useg',
  'match',
  'precedence'],
 'aci_match_as_path_regex_term': ['tenant*',
  'match_rule',
  'match_as_path_regex_term*',
  'regex',
  'description',
  'name_alias',
  'state'],
 'aci_fabric_span_src_group': ['source_group*',
  'description',
  'admin_state',
  'destination_group*',
  'state',
  'name_alias'],
 'aci_aep_to_domain': ['aep*',
  'domain*',
  'domain_type*',
  'state',
  'vm_provider'],
 'aci_aaa_security_default_settings': ['password_strength_check',
  'password_strength_profile',
  'options',
  'enable',
  'type',
  'min_length',
  'max_length',
  'class_flags'],
 'aci_aaa_user_certificate': ['aaa_user*',
  'aaa_user_type',
  'certificate*',
  'name*',
  'state',
  'name_alias'],
 'aci_fabric_pod_remote_pool': ['pod_id*',
  'description',
  'remote_id*',
  'name_alias',
  'remote_pool',
  'state'],
 'aci_config_export_policy': ['name*',
  'description',
  'format',
  'target_dn',
  'snapshot',
  'export_destination',
  'scheduler',
  'start_now',
  'state'],
 'aci_netflow_record_policy': ['tenant*',
  'netflow_record_policy*',
  'collect',
  'match',
  'description',
  'state'],
 'aci_firmware_group_node': ['group*', 'node*', 'state', 'name_alias'],
 'aci_filter': ['filter*', 'tenant*', 'description', 'state', 'name_alias'],
 'aci_fabric_switch_block': ['name*',
  'switch_type',
  'profile*',
  'association*',
  'description',
  'from_node',
  'to_node',
  'state'],
 'aci_esg': ['tenant*',
  'ap*',
  'esg*',
  'admin_state',
  'vrf*',
  'description',
  'intra_esg_isolation'],
 'aci_aep_to_epg': ['aep*',
  'tenant*',
  'ap*',
  'epg*',
  'encap*',
  'primary_encap',
  'interface_mode*'],
 'aci_config_snapshot': ['description',
  'export_policy*',
  'format',
  'include_secure',
  'max_count',
  'snapshot',
  'state'],
 'aci_epg_to_contract_master': ['tenant',
  'ap',
  'epg',
  'contract_master_ap*',
  'contract_master_epg*',
  'state'],
 'aci_fabric_management_access_https_cipher': ['fabric_management_access_policy_name*',
  'id*',
  'cipher_state*',
  'name_alias',
  'state'],
 'aci_interface_policy_lldp': ['lldp_policy*',
  'description',
  'receive_state',
  'transmit_state',
  'state',
  'name_alias'],
 'aci_system_endpoint_controls': ['ip_aging*',
  'options*',
  'admin_state*',
  'roque_ep_control*',
  'options',
  'admin_state',
  'interval',
  'multiplication_factor',
  'hold_interval'],
 'aci_access_spine_switch_selector': ['spine_switch_profile*',
  'spine_switch_selector*'],
 'aci_vmm_uplink_container': ['domain*', 'num_of_uplinks*', 'state'],
 'aci_interface_policy_port_security': ['port_security*',
  'description',
  'max_end_points',
  'port_security_timeout',
  'state',
  'name_alias'],
 'aci_tenant_span_src_group': ['tenant*',
  'src_group*',
  'admin_state',
  'description',
  'dst_group',
  'state',
  'name_alias'],
 'aci_vmm_controller': ['name*',
  'controller_hostname',
  'dvs_version',
  'stats_collection',
  'domain*',
  'state',
  'credentials',
  'inband_management_epg',
  'name_alias',
  'datacenter',
  'vm_provider*'],
 'aci_vmm_uplink': ['domain*', 'uplink_id*', 'uplink_name', 'state'],
 'aci_netflow_monitor_policy': ['tenant*',
  'netflow_monitor_policy*',
  'netflow_record_policy',
  'description',
  'state'],
 'aci_pim_route_map_policy': ['tenant*',
  'pim_route_map_policy*',
  'description',
  'state'],
 'aci_static_binding_to_epg': ['tenant*',
  'ap*',
  'epg*',
  'description',
  'encap_id*',
  'primary_encap_id',
  'deploy_immediacy',
  'interface_mode'],
 'aci_contract_subject': ['tenant*',
  'contract*',
  'subject*',
  'reverse_filter',
  'description',
  'consumer_match',
  'provider_match',
  'state',
  'name_alias',
  'apply_both_direction'],
 'aci_bfd_multihop_node_policy': ['name*',
  'description',
  'admin_state',
  'detection_multiplier',
  'min_transmit_interval',
  'min_receive_interval',
  'state',
  'tenant*'],
 'aci_access_spine_interface_selector': ['spine_interface_profile*',
  'spine_interface_selector*'],
 'aci_match_community_factor': ['tenant*',
  'match_rule*',
  'match_community_term*',
  'community*',
  'scope',
  'description',
  'name_alias',
  'state'],
 'aci_fabric_interface_policy_group': ['name*',
  'description',
  'name_alias',
  'type',
  'dwdm_policy',
  'link_level_policy',
  'link_flap_policy',
  'l3_interface_policy',
  'macsec_policy',
  'monitoring_policy',
  'transceiver_policy_tdn',
  'state'],
 'aci_aaa_key_ring': ['name*',
  'cloud_tenant',
  'description',
  'certificate',
  'modulus',
  'certificate_authority',
  'key',
  'key_type',
  'ecc_curve',
  'state',
  'name_alias'],
 'aci_l3out_floating_svi_path_secondary_ip': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id',
  'node_id',
  'encap',
  'domain_type',
  'domain',
  'secondary_ip*'],
 'aci_l3out_interface_secondary_ip': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id',
  'node_id',
  'path_ep',
  'side',
  'address',
  'ipv6_dad'],
 'aci_interface_policy_hsrp': ['tenant*',
  'hsrp*',
  'description',
  'controls',
  'reload_delay',
  'delay',
  'state'],
 'aci_qos_custom_policy': ['tenant*',
  'qos_custom_policy*',
  'description',
  'state'],
 'aci_interface_policy_l2': ['l2_policy*',
  'description',
  'vlan_scope',
  'qinq',
  'vepa',
  'state',
  'name_alias'],
 'aci_syslog_group': ['name*',
  'format',
  'admin_state',
  'console_logging',
  'console_log_severity',
  'local_file_logging',
  'local_file_log_severity'],
 'aci_filter_entry': ['arp_flag',
  'description',
  'destination_port',
  'destination_port_end',
  'destination_port_start',
  'source_port',
  'source_port_end',
  'source_port_start',
  'tcp_flags',
  'match_only_fragments',
  'entry*',
  'ether_type',
  'filter*',
  'icmp_msg_type',
  'icmp6_msg_type',
  'ip_protocol',
  'state',
  'stateful',
  'tenant*',
  'name_alias'],
 'aci_system_connectivity_preference': ['interface_preference*'],
 'aci_vrf': ['tenant*',
  'vrf*',
  'description',
  'policy_control_direction',
  'policy_control_preference',
  'state',
  'preferred_group',
  'match_type',
  'name_alias',
  'ip_data_plane_learning'],
 'aci_interface_policy_leaf_profile': ['interface_profile*',
  'description',
  'state',
  'name_alias',
  'type'],
 'aci_l3out': ['tenant*',
  'l3out*',
  'domain*',
  'vrf*',
  'description',
  'route_control'],
 'aci_interface_policy_fc': ['fc_policy*',
  'description',
  'port_mode',
  'auto_max_speed',
  'fill_pattern',
  'buffer_credits',
  'speed',
  'trunk_mode',
  'state',
  'name_alias'],
 'aci_fabric_external_connection_profile': ['description',
  'fabric_id*',
  'name',
  'community',
  'site_id',
  'peering_type',
  'peering_password',
  'state'],
 'aci_interface_policy_link_level': ['link_level_policy*',
  'description',
  'auto_negotiation',
  'speed',
  'link_debounce_interval',
  'forwarding_error_correction'],
 'aci_switch_policy_vpc_protection_group': ['protection_group*',
  'protection_group_id*',
  'vpc_domain_policy',
  'switch_1_id*',
  'switch_2_id*',
  'state',
  'name_alias'],
 'aci_tenant_span_src_group_src': ['description',
  'direction*',
  'name*',
  'src_ap',
  'src_epg',
  'src_group*',
  'state',
  'tenant*'],
 'aci_tenant_action_rule_profile': ['action_rule*',
  'tenant*',
  'set_community',
  'set_dampening',
  'set_next_hop',
  'next_hop_propagation',
  'multipath',
  'set_preference',
  'set_metric',
  'set_metric_type',
  'set_route_tag',
  'set_weight',
  'description',
  'state',
  'name_alias'],
 'aci_keychain_policy': ['tenant*',
  'keychain_policy*',
  'description',
  'state'],
 'aci_netflow_monitor_to_exporter': ['tenant*',
  'netflow_monitor_policy*',
  'netflow_exporter_policy*',
  'state'],
 'aci_fabric_pod_profile': ['description', 'state', 'name_alias', 'name*'],
 'aci_interface_policy_leaf_breakout_port_group': ['breakout_port_group*',
  'description',
  'breakout_map',
  'state'],
 'aci_fabric_management_access': ['name*',
  'description',
  'name_alias',
  'http',
  'options',
  'admin_state',
  'port',
  'redirect',
  'allow_origins',
  'allow_credentials',
  'throttle',
  'throttle_rate',
  'throttle_unit'],
 'aci_interface_policy_mcp': ['mcp*',
  'description',
  'admin_state',
  'mcp_mode',
  'grace_period',
  'grace_period_millisec',
  'init_delay_time',
  'tx_frequence',
  'tx_frequence_millisec',
  'state',
  'name_alias'],
 'aci_fabric_span_src_group_src_node': ['source_group*',
  'source*',
  'pod*',
  'node*',
  'state'],
 'aci_interface_policy_storm_control': ['storm_control_policy*'],
 'aci_l3out_hsrp_secondary_vip': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'hsrp_interface_group*',
  'secondary_virtual_ip*',
  'state'],
 'aci_maintenance_policy': ['name*',
  'run_mode',
  'graceful',
  'scheduler*',
  'ignore_compat',
  'admin_state',
  'download_state',
  'notify_condition',
  'smu_operation',
  'smu_operation_flags',
  'sr_upgrade',
  'sr_version',
  'version',
  'version_check_override',
  'description',
  'state',
  'name_alias'],
 'aci_action_rule_set_as_path': ['tenant*',
  'action_rule*',
  'last_as',
  'criteria*',
  'description',
  'state',
  'name_alias'],
 'aci_l3out_floating_svi_secondary_ip': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id',
  'node_id',
  'encap',
  'secondary_ip*'],
 'aci_netflow_exporter_policy': ['tenant*',
  'netflow_exporter_policy*',
  'dscp',
  'destination_address*',
  'destination_port*',
  'source_ip_type',
  'custom_source_address',
  'associated_epg',
  'associated_extepg',
  'associated_vrf',
  'description',
  'state'],
 'aci_interface_policy_leaf_fc_policy_group': ['lag_type',
  'policy_group*',
  'description',
  'fibre_channel_interface_policy',
  'port_channel_policy',
  'attached_entity_profile',
  'state',
  'name_alias'],
 'aci_access_span_filter_group_entry': ['filter_group*',
  'source_ip*',
  'destination_ip*',
  'first_src_port',
  'last_src_port',
  'first_dest_port',
  'last_dest_port',
  'ip_protocol',
  'name_alias',
  'state'],
 'aci_esg_tag_selector': ['tenant*',
  'ap*',
  'esg*',
  'name*',
  'operator',
  'match_value*',
  'description',
  'state'],
 'aci_ap': ['tenant*',
  'ap*',
  'description',
  'state',
  'name_alias',
  'monitoring_policy'],
 'aci_tenant_span_dst_group': ['tenant*',
  'destination_epg*',
  'destination_group*',
  'description',
  'name_alias',
  'source_ip*',
  'destination_ip*',
  'mtu',
  'ttl',
  'flow_id',
  'version_enforced',
  'span_version',
  'dscp'],
 'aci_interface_policy_bfd_multihop': ['name*',
  'description',
  'admin_state',
  'detection_multiplier',
  'min_transmit_interval',
  'min_receive_interval',
  'state',
  'tenant*'],
 'aci_match_community_regex_term': ['tenant*',
  'match_rule*',
  'match_community_regex_term',
  'community_type*',
  'regex',
  'description',
  'name_alias',
  'state'],
 'aci_route_control_profile': ['tenant*',
  'l3out',
  'route_control_profile*',
  'description',
  'auto_continue',
  'policy_type',
  'name_alias',
  'state'],
 'aci_epg_useg_attribute_simple_statement': ['ap*',
  'epg*',
  'state',
  'tenant*',
  'parent_block_statements',
  'name*',
  'type',
  'operator',
  'category',
  'value',
  'use_subnet'],
 'aci_l3out_to_sr_mpls_infra_l3out': ['tenant*',
  'l3out*',
  'description',
  'infra_l3out*',
  'external_epg*',
  'outbound_route_map*',
  'inbound_route_map',
  'state',
  'name_alias'],
 'aci_access_span_src_group_src': ['source_group*',
  'description',
  'source*',
  'direction',
  'filter_group',
  'drop_packets',
  'epg*',
  'options',
  'epg',
  'ap',
  'tenant'],
 'aci_fabric_span_dst_group': ['destination_group*',
  'description',
  'destination_epg*',
  'name_alias',
  'state'],
 'aci_taboo_contract': ['taboo_contract*',
  'tenant*',
  'scope',
  'description',
  'state',
  'name_alias'],
 'aci_fabric_span_src_group_src_path': ['source_group*',
  'source*',
  'pod*',
  'node*',
  'path_ep*',
  'state'],
 'aci_contract': ['contract*',
  'tenant*',
  'description',
  'scope',
  'priority',
  'dscp'],
 'aci_fabric_node': ['description',
  'node_id*',
  'pod_id',
  'role',
  'node_type',
  'remote_leaf_pool_id',
  'serial*',
  'switch',
  'state',
  'name_alias'],
 'aci_interface_policy_eigrp': ['tenant*',
  'eigrp*',
  'description',
  'bandwidth',
  'control_state',
  'delay',
  'delay_unit',
  'hello_interval',
  'hold_interval',
  'state',
  'name_alias'],
 'aci_dhcp_option_policy': ['tenant*',
  'dhcp_option_policy*',
  'description',
  'state'],
 'aci_access_spine_switch_profile': ['switch_profile*'],
 'aci_epg_to_contract_interface': ['tenant*',
  'ap*',
  'epg*',
  'contract_interface*',
  'priority',
  'state'],
 'aci_firmware_group': ['group*',
  'policy*',
  'type_group',
  'description',
  'state',
  'name_alias'],
 'aci_firmware_policy': ['name*',
  'description',
  'version*',
  'effective_on_reboot',
  'ignore_compat',
  'sr_upgrade',
  'sr_version',
  'version_check_override',
  'state',
  'name_alias'],
 'aci_aaa_custom_privilege': ['name*', 'description', 'write_privilege'],
 'aci_bgp_rr_asn': ['asn*', 'state'],
 'aci_bgp_route_summarization_policy': ['tenant*',
  'route_summarization_policy*',
  'address_type_af_control',
  'control_state',
  'description',
  'state',
  'name_alias'],
 'aci_interface_policy_ospf': ['tenant*',
  'ospf*',
  'description',
  'network_type',
  'cost',
  'controls',
  'dead_interval',
  'hello_interval',
  'prefix_suppression',
  'priority',
  'retransmit_interval',
  'transmit_delay',
  'state',
  'name_alias'],
 'aci_dns_provider': ['dns_profile', 'address*', 'preferred', 'state'],
 'aci_snmp_user': ['policy*',
  'name*',
  'description',
  'auth_type',
  'auth_key',
  'privacy_type',
  'privacy_key',
  'state'],
 'aci_l3out_static_routes_nexthop': ['tenant*',
  'l3out*',
  'node_profile*',
  'pod_id*',
  'node_id*',
  'prefix*',
  'nexthop*',
  'state'],
 'aci_epg_to_contract': ['contract_type',
  'ap*',
  'epg*',
  'contract*',
  'priority',
  'provider_match',
  'state',
  'tenant*',
  'contract_label',
  'subject_label'],
 'aci_epg_subnet': ['tenant*',
  'epg*',
  'ap*',
  'description',
  'enable_vip',
  'gateway*',
  'mask*',
  'subnet_name',
  'nd_prefix_policy',
  'preferred',
  'route_profile',
  'route_profile_l3out',
  'scope',
  'subnet_control',
  'state',
  'ip_data_plane_learning',
  'name_alias'],
 'aci_node_mgmt_epg': ['type', 'epg*', 'bd', 'encap', 'state'],
 'aci_vrf_multicast': ['tenant*',
  'vrf*',
  'pim_setting',
  'options',
  'mtu',
  'control_state'],
 'aci_l3out_bgp_protocol_profile': ['tenant*',
  'l3out*',
  'node_profile*',
  'bgp_timers_policy',
  'bgp_best_path_policy',
  'state',
  'name_alias'],
 'aci_encap_pool_range': ['pool_type',
  'allocation_mode',
  'description',
  'pool*',
  'pool_allocation_mode',
  'range_end*',
  'range_name',
  'range_start*',
  'state',
  'name_alias'],
 'aci_access_span_dst_group': ['destination_group*',
  'description',
  'access_interface',
  'destination_epg',
  'name_alias',
  'state'],
 'aci_dns_profile': ['dns_profile*', 'state'],
 'aci_vzany_to_contract': ['tenant*', 'vrf*', 'contract*', 'type', 'state'],
 'aci_switch_policy_leaf_profile': ['leaf_profile*',
  'description',
  'state',
  'name_alias'],
 'aci_contract_subject_to_service_graph': ['tenant*',
  'contract*',
  'subject*',
  'service_graph*',
  'state'],
 'aci_syslog_remote_dest': ['name',
  'format',
  'admin_state',
  'description',
  'destination*',
  'facility',
  'group*',
  'mgmt_epg',
  'syslog_port',
  'severity',
  'state'],
 'aci_vlan_pool_encap_block': ['pool*',
  'block_name',
  'block_end*',
  'block_start*',
  'allocation_mode',
  'description',
  'pool_allocation_mode*',
  'state',
  'name_alias'],
 'aci_system': ['id', 'state'],
 'aci_interface_config': ['policy_group',
  'breakout',
  'description',
  'node*',
  'pc_member',
  'port_type',
  'role',
  'admin_state',
  'interface_type'],
 'aci_pim_route_map_entry': ['tenant*',
  'pim_route_map_policy*',
  'description',
  'order*',
  'source_ip',
  'group_ip',
  'rp_ip',
  'action',
  'state'],
 'aci_l3out_logical_node_profile': ['node_profile*',
  'tenant*',
  'l3out*',
  'description',
  'dscp'],
 'aci_maintenance_group_node': ['group*', 'node*', 'state', 'name_alias'],
 'aci_interface_policy_leaf_profile_fex_policy_group': ['name*',
  'fex_profile*',
  'state'],
 'aci_snmp_policy': ['name*',
  'admin_state',
  'contact',
  'description',
  'location',
  'state'],
 'aci_l3out_floating_svi_path': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id',
  'node_id',
  'encap',
  'floating_ip*',
  'forged_transmit',
  'mac_change',
  'promiscuous_mode',
  'domain_type*',
  'domain*',
  'enhanced_lag_policy',
  'access_encap'],
 'aci_file_remote_path': ['name*',
  'description',
  'remote_host',
  'remote_port',
  'remote_protocol',
  'remote_path',
  'auth_type*',
  'remote_user',
  'remote_password',
  'remote_ssh_key',
  'remote_ssh_passphrase',
  'management_epg',
  'state'],
 'aci_action_rule_additional_communities': ['tenant*',
  'action_rule*',
  'community*',
  'criteria',
  'description',
  'state',
  'name_alias'],
 'aci_maintenance_group': ['group*',
  'policy',
  'firmware_nodes_type',
  'type_group',
  'description',
  'state',
  'name_alias'],
 'aci_bulk_static_binding_to_epg': ['tenant*',
  'ap*',
  'epg*',
  'description',
  'encap_id',
  'primary_encap_id',
  'deploy_immediacy',
  'interface_mode'],
 'aci_tag': ['dn*', 'tag_key*', 'tag_value', 'tag_type', 'state'],
 'aci_fabric_leaf_profile': ['name*', 'description', 'state'],
 'aci_interface_selector_to_switch_policy_leaf_profile': ['leaf_profile*',
  'interface_selector*',
  'state'],
 'aci_access_sub_port_block_to_access_port': ['leaf_interface_profile*',
  'access_port_selector*',
  'leaf_port_blk*',
  'leaf_port_blk_description',
  'from_port*',
  'to_port*',
  'from_sub_port*',
  'to_sub_port*',
  'from_card',
  'to_card',
  'state'],
 'aci_match_route_destination': ['tenant*',
  'match_rule*',
  'ip*',
  'aggregate',
  'from_prefix_length',
  'to_prefix_length',
  'description',
  'name_alias',
  'state'],
 'aci_fabric_span_src_group_src': ['source_group*',
  'description',
  'source*',
  'direction',
  'drop_packets',
  'vrf*',
  'options',
  'vrf',
  'tenant'],
 'aci_aaa_certificate_authority': ['name*'],
 'aci_bd_to_netflow_monitor_policy': ['bd*',
  'netflow_monitor_policy*',
  'filter_type*',
  'tenant*',
  'state'],
 'aci_bd_subnet': ['bd*',
  'description',
  'enable_vip',
  'gateway*',
  'mask*',
  'subnet_name',
  'nd_prefix_policy',
  'preferred',
  'route_profile',
  'route_profile_l3_out',
  'scope',
  'subnet_control',
  'state',
  'tenant*',
  'name_alias',
  'ip_data_plane_learning'],
 'aci_l3out_bfd_multihop_interface_profile': ['tenant*',
  'l3out*',
  'l3out_logical_node_profile*',
  'l3out_logical_interface_profile*',
  'name',
  'name_alias',
  'description',
  'authentication_type',
  'key',
  'key_id',
  'bfd_multihop_interface_policy*',
  'state'],
 'aci_encap_pool': ['pool_type',
  'description',
  'pool*',
  'pool_allocation_mode',
  'state',
  'name_alias'],
 'aci_bgp_rr_node': ['node_id*', 'pod_id*', 'description', 'state'],
 'aci_fabric_pod_connectivity_profile': ['pod_id*',
  'fabric_id*',
  'virtual_pod_id',
  'description',
  'data_plane_tep',
  'unicast_tep',
  'state'],
 'aci_contract_subject_to_filter': ['tenant*',
  'contract*',
  'filter*',
  'subject*',
  'direction',
  'action',
  'directives',
  'priority_override',
  'state'],
 'aci_dns_domain': ['dns_profile', 'domain*', 'default', 'state'],
 'aci_fabric_wide_settings': ['disable_remote_ep_learning',
  'enforce_subnet_check',
  'enforce_epg_vlan_validation',
  'enforce_domain_validation',
  'spine_opflex_client_auth',
  'leaf_opflex_client_auth',
  'spine_ssl_opflex',
  'leaf_ssl_opflex',
  'opflex_ssl_versions',
  'reallocate_gipo',
  'restrict_infra_vlan_traffic',
  'state'],
 'aci_aaa_user_domain': ['aaa_user*',
  'name*',
  'aaa_user_type',
  'name_alias',
  'state'],
 'aci_action_rule_set_as_path_asn': ['tenant*',
  'action_rule*',
  'asn',
  'order*',
  'description',
  'state',
  'name_alias'],
 'aci_domain': ['domain_type*', 'domain*', 'dscp'],
 'aci_match_community_term': ['tenant*',
  'match_rule*',
  'match_community_term*',
  'description',
  'name_alias',
  'state'],
 'aci_access_port_to_interface_policy_leaf_profile': ['interface_profile*',
  'access_port_selector*',
  'description',
  'port_blk',
  'leaf_port_blk_description',
  'from_port',
  'to_port',
  'from_card',
  'to_card',
  'policy_group',
  'interface_type'],
 'aci_l3out_interface': ['tenant',
  'l3out',
  'node_profile',
  'interface_profile',
  'state',
  'pod_id*',
  'node_id*',
  'path_ep*',
  'address',
  'mtu',
  'ipv6_dad',
  'interface_type*',
  'mode',
  'encap',
  'encap_scope',
  'auto_state',
  'description',
  'mac',
  'micro_bfd',
  'micro_bfd_destination',
  'micro_bfd_timer'],
 'aci_fabric_spine_switch_assoc': ['profile*',
  'name*',
  'policy_group',
  'description',
  'state'],
 'aci_interface_policy_cdp': ['cdp_policy*',
  'description',
  'admin_state',
  'state',
  'name_alias'],
 'aci_l3out_extepg_to_contract': ['contract_type',
  'l3out*',
  'contract*',
  'priority',
  'provider_match',
  'state',
  'tenant*',
  'extepg*',
  'contract_label',
  'subject_label'],
 'aci_aaa_role': ['name*',
  'privileges*',
  'description',
  'state',
  'name_alias'],
 'aci_config_rollback': ['compare_export_policy',
  'compare_snapshot',
  'description',
  'export_policy',
  'fail_on_decrypt',
  'import_mode',
  'import_policy',
  'import_type',
  'snapshot',
  'state'],
 'aci_snmp_client_group': ['client_group*',
  'mgmt_epg',
  'policy*',
  'description',
  'state'],
 'aci_tenant_ep_retention_policy': ['tenant*',
  'epr_policy*',
  'bounce_age',
  'bounce_trigger',
  'hold_interval',
  'local_ep_interval',
  'remote_ep_interval',
  'description',
  'move_frequency',
  'state',
  'name_alias'],
 'aci_access_spine_interface_profile': ['interface_profile*'],
 'aci_aaa_domain': ['name*',
  'description',
  'restricted_rbac_domain',
  'state',
  'name_alias'],
 'aci_access_port_block_to_access_port': ['interface_profile*'],
 'aci_ntp_server': ['ntp_policy',
  'ntp_server*',
  'description',
  'min_poll',
  'max_poll',
  'preferred',
  'epg_type',
  'epg_name',
  'state'],
 'aci_bd_to_l3out': ['bd*', 'l3out*', 'tenant*', 'state'],
 'aci_bgp_address_family_context_policy': ['tenant*',
  'address_family_context_policy*',
  'host_route_leak',
  'ebgp_distance',
  'ibgp_distance',
  'local_distance',
  'ebgp_max_ecmp',
  'ibgp_max_ecmp',
  'local_max_ecmp',
  'bgp_add_path_capability',
  'description',
  'state',
  'name_alias'],
 'aci_rest': ['path', 'method', 'src', 'content', 'rsp_subtree_preserve'],
 'aci_access_switch_policy_group': ['name*',
  'description',
  'switch_type',
  'spanning_tree_policy',
  'bfd_ipv4_policy',
  'bfd_ipv6_policy',
  'bfd_multihop_ipv4_policy',
  'bfd_multihop_ipv6_policy',
  'fibre_channel_node_policy',
  'poe_node_policy',
  'fibre_channel_san_policy',
  'monitoring_policy',
  'netflow_node_policy',
  'copp_policy',
  'forward_scale_profile_policy',
  'fast_link_failover_policy',
  'node_802_1x_authentication_policy',
  'copp_pre_filter_policy',
  'equipment_flash_policy',
  'cdp_policy',
  'lldp_policy',
  'sync_e_node_policy',
  'ptp_node_policy',
  'usb_configuration_policy',
  'state'],
 'aci_fabric_pod_selector': ['description',
  'state',
  'name_alias',
  'pod_profile*',
  'name*',
  'type*',
  'blocks',
  'policy_group'],
 'aci_l3out_logical_interface_vpc_member': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'path_dn',
  'pod_id',
  'node_id',
  'path_ep',
  'side*',
  'address',
  'ipv6_dad',
  'description',
  'state',
  'name_alias'],
 'aci_snmp_community_policy': ['community*',
  'policy*',
  'description',
  'state'],
 'aci_tenant': ['tenant*', 'description', 'state', 'name_alias'],
 'aci_snmp_client': ['address*',
  'client_group*',
  'policy*',
  'client_name',
  'state'],
 'aci_qos_dot1p_class': ['tenant*', 'qos_custom_policy*', 'priority'],
 'aci_epg_useg_attribute_block_statement': ['ap*',
  'epg*',
  'state',
  'tenant*',
  'parent_block_statements',
  'name*',
  'match'],
 'aci_route_control_context': ['tenant*',
  'l3out',
  'route_control_profile',
  'route_control_context*',
  'match_rule',
  'action_rule',
  'action',
  'order',
  'description',
  'name_alias',
  'state'],
 'aci_qos_dscp_class': ['tenant*', 'qos_custom_policy*', 'priority'],
 'aci_l2out_extepg_to_contract': ['contract_type',
  'l2out*',
  'contract*',
  'priority',
  'provider_match',
  'state',
  'tenant*',
  'extepg*'],
 'aci_l2out_logical_interface_profile': ['tenant*',
  'l2out*',
  'node_profile*',
  'interface_profile*',
  'state'],
 'aci_l3out_logical_node': ['tenant*',
  'l3out*',
  'node_profile*',
  'pod_id*',
  'node_id*',
  'router_id',
  'router_id_as_loopback',
  'loopback_address',
  'mpls_transport_loopback_address',
  'sid',
  'state'],
 'aci_interface_policy_spanning_tree': ['stp_policy*',
  'description',
  'bpdu_guard',
  'bpdu_filter',
  'state',
  'name_alias'],
 'aci_l3out_eigrp_interface_profile': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'eigrp_policy*',
  'eigrp_keychain_policy',
  'description',
  'state'],
 'aci_interface_policy_leaf_policy_group': ['lag_type',
  'policy_group*',
  'description',
  'link_level_policy',
  'cdp_policy',
  'mcp_policy',
  'lldp_policy',
  'stp_interface_policy',
  'egress_data_plane_policing_policy',
  'ingress_data_plane_policing_policy',
  'priority_flow_control_policy',
  'fibre_channel_interface_policy',
  'slow_drain_policy',
  'port_channel_policy',
  'monitoring_policy',
  'storm_control_interface_policy',
  'l2_interface_policy',
  'port_security_policy',
  'link_flap_policy',
  'link_level_flow_control',
  'mac_sec_interface_policy',
  'copp_policy',
  'aep',
  'sync_e_interface_policy',
  'transceiver_policy',
  'options',
  'name',
  'type'],
 'aci_aaa_user': ['aaa_password',
  'aaa_password_lifetime',
  'aaa_password_update_required',
  'aaa_user*',
  'clear_password_history',
  'description',
  'email',
  'enabled',
  'expiration',
  'expires',
  'first_name',
  'last_name',
  'phone',
  'state',
  'name_alias'],
 'aci_ntp_policy': ['name*',
  'description',
  'admin_state',
  'server_state',
  'auth_state',
  'master_mode',
  'state'],
 'aci_fabric_scheduler': ['name*',
  'description',
  'windowname',
  'recurring',
  'concurCap',
  'maxTime',
  'date',
  'state',
  'hour',
  'minute',
  'day'],
 'aci_aep': ['aep*', 'description', 'infra_vlan', 'state', 'name_alias'],
 'aci_l3out_extepg': ['tenant*',
  'l3out*',
  'extepg*',
  'description',
  'preferred_group',
  'dscp'],
 'aci_fabric_external_routing_profile': ['name*',
  'fabric_id*',
  'description',
  'subnets',
  'state'],
 'aci_bgp_best_path_policy': ['tenant*',
  'bgp_best_path_policy*',
  'best_path_control',
  'description',
  'state',
  'name_alias'],
 'aci_fabric_leaf_switch_assoc': ['profile*',
  'name*',
  'policy_group',
  'description',
  'state'],
 'aci_access_span_src_group': ['source_group*',
  'description',
  'admin_state',
  'filter_group',
  'destination_group*',
  'state',
  'name_alias'],
 'aci_bgp_peer_prefix_policy': ['tenant*',
  'peer_prefix_policy*',
  'action',
  'maximum_number_prefix',
  'restart_time',
  'threshold',
  'description',
  'state',
  'name_alias'],
 'aci_esg_to_contract': ['contract_type',
  'tenant*',
  'ap*',
  'esg*',
  'contract*',
  'priority',
  'state'],
 'aci_fabric_spine_profile': ['name*', 'description', 'state'],
 'aci_node_block': ['switch_profile*'],
 'aci_esg_epg_selector': ['tenant*',
  'ap*',
  'esg*',
  'epg_ap*',
  'epg*',
  'description',
  'state'],
 'aci_aaa_user_role': ['aaa_user*',
  'aaa_user_type',
  'domain_name*',
  'name*',
  'privilege_type',
  'name_alias',
  'state'],
 'aci_dhcp_relay': ['name*', 'description', 'state', 'tenant'],
 'aci_l3out_dhcp_relay_label': ['tenant*',
  'l3out*',
  'node_profile*',
  'interface_profile*',
  'dhcp_relay_label*',
  'scope',
  'dhcp_option_policy',
  'description',
  'state'],
 'aci_aaa_ssh_auth': ['aaa_user', 'auth_name*', 'data*', 'state'],
 'aci_epg_monitoring_policy': ['monitoring_policy*',
  'tenant*',
  'description',
  'state',
  'name_alias'],
 'aci_interface_policy_port_channel': ['port_channel*',
  'description',
  'min_links',
  'max_links',
  'mode',
  'fast_select',
  'graceful_convergence',
  'load_defer',
  'suspend_individual',
  'symmetric_hash',
  'state',
  'name_alias'],
 'aci_access_span_filter_group': ['filter_group*', 'name_alias', 'state'],
 'aci_l2out_extepg': ['l2out*',
  'description',
  'extepg*',
  'preferred_group',
  'state',
  'tenant*',
  'qos_class'],
 'aci_interface_description': ['pod_id*',
  'node_id*',
  'fex_id',
  'node_type',
  'interface*',
  'description*',
  'state'],
 'aci_l3out_route_tag_policy': ['tenant*',
  'rtp*',
  'description',
  'tag',
  'state',
  'name_alias'],
 'aci_epg_to_domain': ['allow_useg',
  'ap*',
  'deploy_immediacy',
  'domain*',
  'domain_type*',
  'encap',
  'encap_mode',
  'switching_mode',
  'epg*',
  'enhanced_lag_policy',
  'vmm_uplink_active',
  'vmm_uplink_standby',
  'netflow',
  'primary_encap',
  'resolution_immediacy',
  'state',
  'tenant*',
  'vm_provider',
  'promiscuous',
  'custom_epg_name',
  'delimiter',
  'untagged_vlan',
  'port_binding',
  'port_allocation',
  'number_of_ports',
  'forged_transmits',
  'mac_changes'],
 'aci_fabric_node_control': ['name',
  'description',
  'enable_dom',
  'feature_selection',
  'state'],
 'aci_interface_policy_spine_policy_group': ['policy_group*',
  'description',
  'name_alias',
  'link_level_policy',
  'link_flap_policy',
  'cdp_policy',
  'mac_sec_policy',
  'attached_entity_profile',
  'state'],
 'aci_l2out_logical_node_profile': ['tenant*',
  'l2out*',
  'node_profile*',
  'state'],
 'aci_static_node_mgmt_address': ['node_id*',
  'pod_id',
  'type',
  'epg*',
  'ipv4_address*',
  'ipv4_gw*',
  'ipv6_address',
  'ipv6_gw',
  'state'],
 'aci_access_span_src_group_src_path': ['source_group*',
  'source*',
  'pod*',
  'nodes*',
  'path_ep*',
  'state'],
 'aci_fabric_pod_external_tep': ['description',
  'name_alias',
  'pod_id*',
  'external_tep_pool*',
  'reserve_address_count',
  'status',
  'state'],
 'aci_dhcp_option': ['tenant*',
  'dhcp_option_policy*',
  'dhcp_option*',
  'data',
  'id',
  'state'],
 'aci_dhcp_relay_provider': ['relay_policy*',
  'epg_type*',
  'anp',
  'epg',
  'l2out_name',
  'l3out_name',
  'external_epg',
  'dhcp_server_addr',
  'state',
  'tenant',
  'provider_tenant',
  'dn'],
 'aci_bd': ['arp_flooding',
  'bd*',
  'bd_type',
  'description',
  'enable_multicast',
  'enable_routing',
  'endpoint_clear',
  'endpoint_move_detect',
  'endpoint_retention_action',
  'endpoint_retention_policy',
  'igmp_snoop_policy',
  'ip_learning',
  'ipv6_nd_policy',
  'l2_unknown_unicast',
  'l3_unknown_multicast',
  'ipv6_l3_unknown_multicast',
  'limit_ip_learn',
  'mac_address',
  'multi_dest',
  'state',
  'tenant*',
  'vrf',
  'route_profile',
  'route_profile_l3out',
  'name_alias',
  'host_based_routing',
  'enable_rogue_except_mac',
  'allow_intersite_bum_traffic',
  'allow_intersite_l2_stretch',
  'allow_ipv6_multicast',
  'link_local_address',
  'multicast_arp_drop',
  'vmac',
  'optimize_wan_bandwidth',
  'mld_snoop_policy',
  'igmp_policy',
  'vlan',
  'monitoring_policy',
  'first_hop_security_policy',
  'pim_source_filter',
  'pim_destination_filter'],
 'aci_vrf_leak_internal_subnet': ['tenant',
  'vrf',
  'leak_to*',
  'options',
  'vrf',
  'tenant'],
 'aci_esg_ip_subnet_selector': ['tenant*',
  'ap*',
  'esg*',
  'ip*',
  'description',
  'state'],
 'aci_syslog_source': ['name*',
  'include',
  'min_severity',
  'destination_group',
  'state'],
 'aci_bd_dhcp_label': ['bd*',
  'description',
  'dhcp_label*',
  'dhcp_option',
  'scope*',
  'state',
  'tenant*'],
 'aci_igmp_interface_policy': ['name*',
  'tenant*',
  'description',
  'group_timeout',
  'query_interval',
  'query_response_interval',
  'last_member_count',
  'last_member_response',
  'startup_query_count',
  'startup_query_interval',
  'querier_timeout',
  'robustness_variable',
  'igmp_version',
  'allow_v3_asm',
  'fast_leave',
  'report_link_local_groups',
  'state'],
 'aci_vmm_credential': ['name',
  'credential_password',
  'credential_username',
  'description',
  'domain*',
  'state',
  'vm_provider',
  'name_alias'],
 'aci_interface_blacklist': ['pod_id*',
  'node_id*',
  'fex_id',
  'interface*',
  'state'],
 'aci_system_global_aes_passphrase_encryption': ['passphrase',
  'enable',
  'state'],
 'aci_match_rule': ['tenant*',
  'match_rule*',
  'description',
  'name_alias',
  'state'],
 'aci_l3out_bfd_interface_profile': ['tenant*',
  'l3out*',
  'l3out_logical_node_profile*',
  'l3out_logical_interface_profile*',
  'name',
  'name_alias',
  'description',
  'authentication_type',
  'key',
  'key_id',
  'bfd_interface_policy*',
  'state'],
 'aci_l2out_logical_interface_path': ['tenant*',
  'l2out*',
  'node_profile*',
  'interface_profile*',
  'interface_type',
  'pod_id*',
  'leaves*',
  'interface*',
  'state'],
 'aci_firmware_source': ['source*',
  'polling_interval',
  'url*',
  'url_username',
  'url_password',
  'url_protocol*',
  'state',
  'name_alias'],
 'aci_bd_rogue_exception_mac': ['bd*',
  'tenant*',
  'mac*',
  'description',
  'state']}