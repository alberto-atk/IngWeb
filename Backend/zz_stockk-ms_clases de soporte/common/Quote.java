
package fs.stockk.ms.common;

import com.google.gson.Gson;
import java.io.Serializable;

/**
 *
 * @author fserna
 * 
 * 
 * Info from : https://iextrading.com/developer/docs/#last
 * 
 */
public class Quote implements Serializable{
    private String symbol;  // refers to the stock ticker.

    private double price;   // refers to last sale price of the stock on IEX
    private int size;       // refers to last sale size of the stock on IEX.
    private long time;      // refers to last sale time in epoch time of the stock on IEX.
    
    private Long msRx = System.currentTimeMillis();
    
    
    
    
    
    /**
     * @return the symbol
     */
    public String getSymbol() {
        return symbol;
    }

    /**
     * @param symbol the symbol to set
     */
    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    /**
     * @return the price
     */
    public double getPrice() {
        return price;
    }

    /**
     * @param price the price to set
     */
    public void setPrice(double price) {
        this.price = price;
    }

    /**
     * @return the size
     */
    public int getSize() {
        return size;
    }

    /**
     * @param size the size to set
     */
    public void setSize(int size) {
        this.size = size;
    }

    /**
     * @return the time
     */
    public long getTime() {
        return time;
    }

    /**
     * @param time the time to set
     */
    public void setTime(long time) {
        this.time = time;
    }

    /**
     * @return the msRx
     */
    public Long getMsRx() {
        return msRx;
    }

    /**
     * @param msRx the msRx to set
     */
    public void setMsRx(Long msRx) {
        this.msRx = msRx;
    }


    
    
    
    
        /** returns the number of milliseconds ellapsed since this quote was fetched
     * 
     * @return 
     */
    public long howOldAmI(){
       long now = System.currentTimeMillis();
       return (now-this.getMsRx());
    }
    
     
    public String toJson(){
        Gson gson = new Gson();
        String json = gson.toJson(this);
        return json;
    }

}
