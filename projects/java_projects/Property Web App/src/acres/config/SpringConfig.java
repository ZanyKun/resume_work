package acres.config;

import java.io.IOException;
import java.util.Properties;

import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Environment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.support.PropertySourcesPlaceholderConfigurer;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.view.InternalResourceViewResolver;

import acres.dto.BuildingInfo;
import acres.dto.ComBuildingType;
import acres.dto.ReBuildingType;
import acres.dto.UserInfo;
import acres.filter.RequestFilter;

@EnableWebMvc
@Configuration
@PropertySource("classpath:database.properties")
@ComponentScan(basePackages = {"acres"})
public class SpringConfig implements WebMvcConfigurer{
	
	@Value("${hbm2ddl}") String hbm2ddl;
	@Value("${url}") String url;
	@Value("${name}") String username;
	@Value("${password}") String password;
	@Value("${driver}") String driver;
	@Value("${dialect}") String dialect;
	@Bean
	public SessionFactory sessionFatory() throws IOException {
		LocalSessionFactoryBean sf= new LocalSessionFactoryBean();
		sf.setDataSource(datasource());
		Properties p= new Properties();
		p.setProperty(Environment.HBM2DDL_AUTO, hbm2ddl);
		p.setProperty(Environment.SHOW_SQL, "true");
		p.setProperty(Environment.DIALECT, dialect);
		sf.setHibernateProperties(p);
		sf.setAnnotatedClasses(UserInfo.class, BuildingInfo.class, ReBuildingType.class, ComBuildingType.class);
		sf.setAnnotatedPackages("acres.java.dto");
		sf.afterPropertiesSet();
		return sf.getObject();
	}
	
	@Bean
	public DataSource datasource() {
		DriverManagerDataSource ds= new DriverManagerDataSource(url, username, password);
		ds.setDriverClassName(driver);
		return ds;
	}
	
	@Bean
	public static PropertySourcesPlaceholderConfigurer pc() {
		PropertySourcesPlaceholderConfigurer pc= new PropertySourcesPlaceholderConfigurer();
		return pc;
	}
	
	@Override
	public void addResourceHandlers(ResourceHandlerRegistry registry) {
		registry.addResourceHandler("/css").addResourceLocations("css/");
		registry.addResourceHandler("/js").addResourceLocations("js/");
		registry.addResourceHandler("/img").addResourceLocations("img/");
		registry.addResourceHandler("/scss").addResourceLocations("scss/");
	}
	
	@Bean
	public ViewResolver resolver() {
		return new InternalResourceViewResolver("/WEB-INF/",".jsp");
	}

	@Override
	public void addViewControllers(ViewControllerRegistry registry) {
		registry.addViewController("/").setViewName("welcome");
		registry.addViewController("/welcome").setViewName("welcome");
		registry.addViewController("/login").setViewName("login");
		registry.addViewController("/register").setViewName("register");
		registry.addViewController("/list_properties").setViewName("list_properties");
	}
	
	@Override
	public void addInterceptors(InterceptorRegistry registry) {
		registry.addInterceptor(new RequestFilter()).addPathPatterns("*.test");
	}
}