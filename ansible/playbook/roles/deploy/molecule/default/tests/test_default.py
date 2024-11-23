import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    ".molecule/ansible_inventory"
).get_hosts("all")

def test_cluster_deployment(host):
    # Test if Kubernetes is installed
    k8s = host.run("kubectl version")
    assert k8s.rc == 0

    # Test if cluster is deployed
    cluster = host.run("kubectl get clusters -A")
    assert cluster.rc == 0
