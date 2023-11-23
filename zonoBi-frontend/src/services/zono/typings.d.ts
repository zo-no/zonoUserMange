declare namespace API {
  type articleCreate = {
    /** Title */
    title: string;
    /** Channels Id */
    channels_id: number;
    /** Content */
    content: string;
    /** Owner Id */
    owner_id: number;
  };

  type BodyLoginApiV1LoginAccountPost = {
    /** Grant Type */
    grant_type?: string;
    /** Username */
    username: string;
    /** Password */
    password: string;
    /** Scope */
    scope?: string;
    /** Client Id */
    client_id?: string;
    /** Client Secret */
    client_secret?: string;
  };

  type GetToken = {
    /** Access Token */
    access_token: string;
    /** Token Type */
    token_type: string;
    /** Status */
    status: string;
  };

  type HTTPValidationError = {
    /** Detail */
    detail?: ValidationError[];
  };

  type UserInDB = {
    /** Username */
    username: string;
    /** Password 密码 */
    password: string;
  };

  type ValidationError = {
    /** Location */
    loc: any[];
    /** Message */
    msg: string;
    /** Error Type */
    type: string;
  };
}
