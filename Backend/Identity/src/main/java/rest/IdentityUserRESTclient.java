package rest;

import identity.RESTstockkService;
import javax.ws.rs.ClientErrorException;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.WebTarget;

/**
 * Jersey REST client generated for REST resource:UserRESTService [user]<br>
 * USAGE:
 * <pre>
 *        IdentityUserRESTclient client = new IdentityUserRESTclient();
 *        Object response = client.XXX(...);
 *        // do whatever with response
 *        client.close();
 * </pre>
 *
 * @author fsern
 */
public class IdentityUserRESTclient {

    private WebTarget webTarget;
    private Client client;
    private String BASE_URI = "";

    public IdentityUserRESTclient() {
        ServicesDirectoryRESTclient directoryRESTclient = new ServicesDirectoryRESTclient();
        RESTstockkService identityService = directoryRESTclient.getService("stockk_IDENTITY");
        directoryRESTclient.close();
        if (identityService!=null){
            BASE_URI = identityService.getUri();
        }
        client = javax.ws.rs.client.ClientBuilder.newClient();
        webTarget = client.target(BASE_URI).path("user");
    }
    

    public <T> T getUser(Class<T> responseType, String _token) throws ClientErrorException {
        WebTarget resource = webTarget;
        resource = resource.path(java.text.MessageFormat.format("{0}", new Object[]{_token}));
        return resource.request(javax.ws.rs.core.MediaType.APPLICATION_JSON).get(responseType);
    }

    public void createUser(Object requestEntity, String _clearPasswd) throws ClientErrorException {
        webTarget.path(java.text.MessageFormat.format("{0}", new Object[]{_clearPasswd})).request(javax.ws.rs.core.MediaType.APPLICATION_JSON).post(javax.ws.rs.client.Entity.entity(requestEntity, javax.ws.rs.core.MediaType.APPLICATION_JSON));
    }

    public String changePassword(String _token, String _clearPasswd) throws ClientErrorException {
        return webTarget.path(java.text.MessageFormat.format("{0}/{1}", new Object[]{_token, _clearPasswd})).request().put(null, String.class);
    }

    public void close() {
        client.close();
    }
    
}
