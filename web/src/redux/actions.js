import { querySuccess, queryPending, queryError } from "./reducers";

const fetch = (url, payload) => {
    return new Promise(async (resolve, reject) => {
        try {
            const res = await axios.post(url, payload);

            resolve(res.data);
        } catch (error) {
            reject(error.message);
        }
    });
};

export const query = (formData, rowid) => async (dispatch) => {
    try {
        dispatch(queryPending());

        const result = await fetch();
        if (result.length) return dispatch(querySuccess(result));

        dispatch(queryError("No data"));
    } catch (error) {
        dispatch(queryError(error));
    }
};
