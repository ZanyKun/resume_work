package acres.dao;

import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import acres.dto.UserInfo;

@Repository
public class UserRepositoryImpl implements UserRepository{
	
	@Autowired SessionFactory sf;
	
	@Override
	public boolean insertUser(UserInfo c) {
		Session s = sf.openSession();
		s.beginTransaction();
		s.save(c);
		s.getTransaction().commit();
		return true;
	}

	@Override
	public boolean deleteUser(UserInfo c) {
		Session s = sf.openSession();
		s.beginTransaction();
		Query<?> q = s.createQuery("delete from UserInfo where username = ?");
		q.setParameter(1, c.getUsername());
		int retVal = q.executeUpdate();
		s.getTransaction().commit();
		return retVal==1;
	}

	@Override
	public boolean updateUser(UserInfo c) {
		Session s = sf.openSession();
		s.beginTransaction();
		s.update(c);
		s.getTransaction().commit();
		return true;
	}

	@Override
	public UserInfo getUser(String username) {
		Session s = sf.openSession();
		UserInfo user = s.get(UserInfo.class, username);
		return user;
	}

	@SuppressWarnings("unchecked")
	@Override
	public List<UserInfo> getAllUsers() {
		Session s = sf.openSession();
		Query<?> q = s.createQuery("select from UserInfo");
		List<UserInfo> retList = (List<UserInfo>) q.list();
		return retList;
	}

}
