import { actionCreator } from "~/store/actions";
import * as C from "~/constants";
import { api } from "~/helpers";

export const removeStart = () => {
  return actionCreator(C.IVA_ALIQUOTE_REMOVE_START);
};

export const removeFail = (data) => {
  return actionCreator(C.IVA_ALIQUOTE_REMOVE_FAIL, data);
};

export const removeSuccess = (data) => {
  return actionCreator(C.IVA_ALIQUOTE_REMOVE_SUCCESS, data);
};

export const remove = (id) => {
  return (dispatch) => {
    dispatch(removeStart);

    api
      .delete(`/tributi/iva/aliquote/${id}/`)
      .then((response) => {
        dispatch(removeSuccess(id));
      })
      .catch((error) => {
        dispatch(removeFail(error.message));
      });
  };
};
