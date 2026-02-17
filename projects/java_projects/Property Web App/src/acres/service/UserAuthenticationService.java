package acres.service;

import acres.dto.UserInfo;

public interface UserAuthenticationService {
	boolean registerNewUser(UserInfo user);
	boolean authenticateUser(UserInfo user);
}
