
package fs.stockk.ms.common;

import com.google.gson.Gson;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;


public class RESThistory implements Serializable {

    
    
    private String login;
    private List<RESTstock> stocks;
    

    public RESThistory() {
        this.stocks = new ArrayList();
    }
            
            
            
    public String getLogin() {
        return login;
    }

    public void setLogin(String _login) {
        this.login = _login;
    }
    
    
    public void setStocks(List <RESTstock> _stocks){
        this.stocks = _stocks;
    }

    
    public void addStock (RESTstock _s){
        this.stocks.add(_s);
    }
    
     public void removeStock (RESTstock _s){
        this.stocks.remove(_s);
    }
    
    
    public double ggetValueBuy(){
        double v = 0.0;
        for (RESTstock s: this.stocks){
            v += s.getPriceBuy()*s.getNumShares();
        }
        return v;
    }

    public double ggetValueSold(){
        double v = 0.0;
        for (RESTstock s: stocks){
            v += s.getPriceSold()*s.getNumShares();
        }
        return v;
    }


    public double ggetFeesBuy(){
        double v = 0.0;
        for (RESTstock s: this.stocks){
            v += s.getFeeBuy();
        }
        return v;
    }
    
    public double ggetFeesSold(){
        double v = 0.0;
        for (RESTstock s: this.stocks){
            v += s.getFeeSold();
        }
        return v;
    }

    
    public Double ggetProfit(){
        return this.ggetValueSold()-this.ggetValueBuy();
    }
    
    public Double ggetProfitPerc(){
        Double perc = 0.0;
        if (this.ggetValueBuy()>0.0){
            perc = (this.ggetProfit()/this.ggetValueBuy())*100.0;
        }
        return perc;
    }
   
   
    
   public RESTstock getStock(int _id){
        return this.stocks.get(_id);
    }
   
    public Collection<RESTstock> getStocks(){
        return this.stocks;
    }
    
    
    public Collection<String> ggetTickers(){
        Collection<String> tickers =new HashSet();
        for (RESTstock s: this.stocks){
            tickers.add(s.getTicker());
        }
        return tickers;
    }
    
    public String getTextTickers(){
        String tickers ="";
        for (String s: this.ggetTickers()){
            tickers = tickers + s + ",";
        }
        return tickers;
    }
    
    public String toJson(){
        Gson gson = new Gson();
        return gson.toJson(this);
    }

    
    
}
