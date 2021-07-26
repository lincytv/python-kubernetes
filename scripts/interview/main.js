const k8s = require('@kubernetes/client-node');

const kconf = new k8s.KubeConfig();

kconf.loadFromDefault();

const k8sApi = kconf.makeApiClient(k8s.CoreV1Api);

k8sApi.listNode().then(( res ) => {
 for i in k8sApi.listNode()
   console.log(i.items)

});