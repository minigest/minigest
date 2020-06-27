import { actionCreator } from "~/store/actions";
import * as C from "~/constants";
import { api } from "~/helpers";

export const removeStart = () => {
  return actionCreator(C.REGIME_FISCALE_REMOVE_START);
};

export const removeFail = (data) => {
  return actionCreator(C.REGIME_FISCALE_REMOVE_FAIL, data);
};

export const removeSuccess = (data) => {
  return actionCreator(C.REGIME_FISCALE_REMOVE_SUCCESS, data);
};

export const remove = (id) => {
  return (dispatch) => {
    dispatch(removeStart);

    api
      .delete(`${C.REGIME_FISCALE_API_ENDPOINT}${id}/`)
      .then((response) => {
        dispatch(removeSuccess(id));
      })
      .catch((error) => {
        dispatch(removeFail(error.message));
      });
  };
};