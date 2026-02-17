package acres.dao;

import java.util.List;

import acres.dto.UserInfo;

public interface UserRepository {
	public boolean insertUser(UserInfo c);
	public boolean deleteUser(UserInfo c);
	public boolean updateUser(UserInfo c);
	public UserInfo getUser(String username);
	public List<UserInfo> getAllUsers();
}
