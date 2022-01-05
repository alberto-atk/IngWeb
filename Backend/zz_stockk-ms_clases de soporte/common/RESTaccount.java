
package fs.stockk.ms.common;

import com.google.gson.Gson;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author fsernafortea
 */
public class RESTaccount  implements Serializable{

    private String login;
    private Double balance;
    private List<RESTapunte> apuntes;
    
    
    public RESTaccount(){
        apuntes = new ArrayList();
    }

    /**
     * @return the login
     */
    public String getLogin() {
        return login;
    }

    /**
     * @param login the login to set
     */
    public void setLogin(String login) {
        this.login = login;
    }
 
    public Double getBalance() {
        return balance;
    }

    public void setBalance(Double balance) {
        this.balance = balance;
    }
    /**
     * @return the apuntes
     */
    public List<RESTapunte> getApuntes() {
        return apuntes;
    }

    public void setApuntes(List<RESTapunte> _apuntes){
        this.apuntes = _apuntes;
    }
    
    /**
     * @param apuntes the apuntes to set
     */
    public void addApunte(RESTapunte _apunte) {
        this.balance += _apunte.getAmount();
        _apunte.setSaldo(this.balance);
        this.apuntes.add(_apunte);
    }    
    
    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);
    }
    
}
