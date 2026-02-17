package acres.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import acres.dao.UserRepository;
import acres.dto.UserInfo;

@Service
public class UserRetrievalServiceImpl implements UserRetrievalService{
	
	@Autowired UserRepository urep;
	
	@Override
	public UserInfo retrieveUser(UserInfo user) {
		return urep.getUser(user.getUsername());
	}

}
