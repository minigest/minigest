import { actionCreator } from "~/store/actions";
import * as C from "~/constants";
import { api } from "~/helpers";

export const getStart = () => actionCreator(C.IVA_ALIQUOTE_GET_START);
export const getFail = (data) => actionCreator(C.IVA_ALIQUOTE_GET_FAIL, data);
export const getSuccess = (data) => {
  return actionCreator(C.IVA_ALIQUOTE_GET_SUCCESS, data);
};

export const get = () => {
  return (dispatch) => {
    dispatch(getStart);

    api
      .get("/tributi/iva/aliquote/")
      .then((response) => {
        dispatch(getSuccess(response.data));
      })
      .catch((error) => {
        dispatch(getFail(error));
      });
  };
};