import { actionCreator } from "src/state/actions";
import * as C from "src/constants";
import { api } from "src/helpers";

export const getStart = () => {
  return actionCreator(C.TUR_GET_START);
};

export const getFail = (data) => {
  return actionCreator(C.TUR_GET_FAIL, data);
};

export const getSuccess = (data) => {
  return actionCreator(C.TUR_GET_SUCCESS, data);
};

export const get = () => {
  return (dispatch) => {
    dispatch(getStart());

    api
      .get(C.TUR_API_ENDPOINT)
      .then((response) => {
        dispatch(getSuccess(response.data));
      })
      .catch((error) => {
        dispatch(getFail(error.message));
      });
  };
};
