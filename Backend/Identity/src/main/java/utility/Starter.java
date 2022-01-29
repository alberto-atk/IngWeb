package utility;

import common.StatusCode;
import db.UserDB;
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.ejb.EJB;
import javax.ejb.Singleton;
import javax.ejb.Startup;

/**
 *
 * @author fserna
 */
@Singleton
@Startup
public class Starter {

    @EJB TouchTimer timer;
    
	
	// === método que se ejecutará inmediatamente antes de arrancar la aplicación ==
	// aprovecha para realizar el primer registro con el estado "BOOTING".
    @PostConstruct
    public void init(){         
        timer.touch(StatusCode.BOOTING); // <<== método "touch" realiza el registro en 'servicesDirectory'
        System.out.println ("==============================================");       
        System.out.println ("======= Stockk === Identity Service is UP!");       
        System.out.println ("==============================================");       
    }
    
    
    
	// === método que se ejecutará inmediatamente antes de FINALIZAR la aplicación ==
	// aprovecha para refrescar el registro con el estado "DOWN".
    @PreDestroy
    public void byeBye(){
        timer.touch(StatusCode.DOWN); // <<== método "touch" realiza el registro en 'servicesDirectory'
        System.out.println ("------------------------------------------------");       
        System.out.println("======= Stockk === Identity Service is DOWN!");    
        System.out.println ("------------------------------------------------");       
    }
}
