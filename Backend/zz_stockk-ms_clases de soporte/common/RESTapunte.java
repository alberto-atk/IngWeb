
package fs.stockk.ms.common;

import com.google.gson.Gson;
import java.io.Serializable;

/**
 *
 * @author fsernafortea
 */
public class RESTapunte  implements Serializable{
    private Long ms;
    private Double amount;
    private String txt;
    private Double saldo;

    

    /**
     * @return the ms
     */
    public Long getMs() {
        return ms;
    }

    /**
     * @param ms the ms to set
     */
    public void setMs(Long ms) {
        this.ms = ms;
    }

    /**
     * @return the importe
     */
    public Double getAmount() {
        return amount;
    }

    /**
     * @param _amount the importe to set
     */
    public void setAmount(Double _amount) {
        this.amount = _amount;
    }
    
    public String getTxt() {
        return txt;
    }

    public void setTxt(String txt) {
        this.txt = txt;
    }

    /**
     * @return the saldo
     */
    public Double getSaldo() {
        return saldo;
    }

    /**
     * @param _balance the saldo to set
     */
    public void setSaldo(Double _balance) {
        this.saldo = _balance;
    }    
    
    
    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);                
    }
}
