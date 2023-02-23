import sky
from sky import backends
from sky import global_user_state
from sky import spot

def _mock_cluster_state():
    print("==Step 1==")
    handle = backends.CloudVmRayBackend.ResourceHandle(
        cluster_name='test-cluster1',
        cluster_yaml='/tmp/cluster1.yaml',
        launched_nodes=1,
        launched_resources=sky.Resources(sky.AWS(),
                                         instance_type='p3.2xlarge',
                                         region='us-east-1'),
    )

    print("==Step 2==")
    global_user_state.add_or_update_cluster(
        'test-cluster1',
        handle,
        requested_resources={handle.launched_resources},
        ready=False)


if __name__ == '__main__':
    _mock_cluster_state()
