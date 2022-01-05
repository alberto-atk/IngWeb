
package fs.stockk.ms.common;

import com.google.gson.Gson;
import java.io.Serializable;

/**
 *
 * @author fsernafortea
 */
public class RESTbotRule  implements Serializable{

    public RESTbotRule(){
        
    }
    
    
    /**
     * @return the user
     */
    public String getUser() {
        return user;
    }

    /**
     * @param user the user to set
     */
    public void setUser(String user) {
        this.user = user;
    }

    /**
     * @return the ticker
     */
    public String getTicker() {
        return ticker;
    }

    /**
     * @param ticker the ticker to set
     */
    public void setTicker(String ticker) {
        this.ticker = ticker;
    }

    /**
     * @return the enabled
     */
    public Boolean getEnabled() {
        return enabled;
    }

    /**
     * @param enabled the enabled to set
     */
    public void setEnabled(Boolean enabled) {
        this.enabled = enabled;
    }

    /**
     * @return the buyBellow
     */
    public Double getBuyBelow() {
        return buyBelow;
    }    
    public Double getBuyBellow() {
        return buyBelow;
    }

    /**
     * @param _buyBelow the buyBellow to set
     */
    public void setBuyBelow(Double _buyBelow) {
        this.buyBelow = _buyBelow;
    }
    public void setBuyBellow(Double _buyBelow) {
        this.buyBelow = _buyBelow;
    }

    /**
     * @return the sellAbove
     */
    public Double getSellAbove() {
        return sellAbove;
    }

    /**
     * @param sellAbove the sellAbove to set
     */
    public void setSellAbove(Double sellAbove) {
        this.sellAbove = sellAbove;
    }
    private String user;
    private String ticker;
    private Boolean enabled;
    private Double buyBelow;
    private Double sellAbove;

    
    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);                
    }
}
