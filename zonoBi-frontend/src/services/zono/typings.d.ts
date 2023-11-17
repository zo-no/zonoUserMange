declare namespace API {
  type articleCreate = {
    /** Title */
    title: string;
    /** Channels Id */
    channels_id: number;
    /** Content */
    content: string;
  };

  type BodyLoginApiV1TokenPost = {
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

  type HTTPValidationError = {
    /** Detail */
    detail?: ValidationError[];
  };

  type Token = {
    /** Access Token */
    access_token: string;
    /** Token Type */
    token_type: string;
  };

  type User = {
    /** Username */
    username: string;
    /** Id */
    id: number;
    /** Is Active */
    is_active: boolean;
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
