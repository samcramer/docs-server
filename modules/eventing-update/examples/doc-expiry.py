#Please replace the following placeholder code with valid example code

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import time
cluster = Cluster('couchbase://localhost:8091')
authenticator = PasswordAuthenticator('Administrator', 'password')
cluster.authenticate(authenticator)

cb = cluster.open_bucket('source')
cb.upsert('SampleDocument2', {'a_key': 'a_value'})
cb.touch('SampleDocument2', ttl=10*60)

function OnUpdate(doc, meta) {
 if (meta.expiration > 0 ) //do only for those documents that have a non-zero TTL
     {
       var expiry = new Date(meta.expiration);
       // Compute 2 minutes from the TTL timestamp
        var twoMinsPrior = new Date(expiry.setMinutes(expiry.getMinutes()-2));
        var context = {docID : meta.id};
        createTimer(DocTimerCallback, twoMinsPrior , meta.id, context);
        log('Added Doc Timer to DocId:', meta.id);
      }
}
function DocTimerCallback(context)
     {
       log('DocTimerCallback Executed for DocId:', String(context.docID));
       tgt[context.docID] = "To Be Expired Key's Value is:" + JSON.stringify(src[context.docID]);
       log('Doc Timer Executed for DocId', String(context.docID));
     }
