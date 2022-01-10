
package identity;


import com.google.gson.Gson;
import java.io.Serializable;

/**
 * This user is meant to be the REST payload.
 * It does not contain the DB primaryKey, password, nor the privateKey.
 * 
 * @author fserna
 */
public class RESTuser implements Serializable {

    private String login;
    private String name;
    private byte[] publicKey;
    
                                    
    public RESTuser(){
        
    }
    
    public RESTuser(String _login, String _name, byte[] _publicKey){
        this.login      = _login;
        this.name       = _name;
        this.publicKey  = _publicKey;
    }
    
  /**
     * @return the login
     */
    public String getLogin() {
        return login;
    }


    
    /**
     * @return the name
     */
    public String getName() {
        return name;
    }



    /**
     * @return the publicKey
     */
    public byte[] getPublicKey() {
        return publicKey;
    }



    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);
    }

    /**
     * @param login the login to set
     */
    public void setLogin(String login) {
        this.login = login;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @param publicKey the publicKey to set
     */
    public void setPublicKey(byte[] publicKey) {
        this.publicKey = publicKey;
    }

}
