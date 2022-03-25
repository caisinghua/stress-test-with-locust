variable "node_size" {
    description = "Size of total nodes"
    default = 4
}

variable "leader_instance_type" {
    default = "t3.micro"
}

variable "nodes_intance_type" {
    default = "t3.micro"
}

variable "loadtest_dir_source" {
    default = "plan/"
}

variable "locust_plan_filename" {
    default = "locustfile.py"
}

variable "subnet_name" {
    default = "VpcDevelopmentStack/VpcStack/PublicSubnet1"
    description = "Subnet name"
}