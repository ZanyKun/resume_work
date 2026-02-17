package acres.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import acres.dao.UserRepository;
import acres.dto.UserInfo;

@Service
public class UserAuthenticationServiceImpl implements UserAuthenticationService{

	@Autowired
	UserRepository userRepo;
	
	@Override
	public boolean registerNewUser(UserInfo user) {
		return userRepo.insertUser(user);
	}

	@Override
	public boolean authenticateUser(UserInfo user) {
		return (userRepo.getUser(user.getUsername()) == null);
	}

}
