import { createSlice } from '@reduxjs/toolkit';

const initialState = {
	isLoading: false,
	songs: [],
};

const querySlice = createSlice({
	name: 'query',
	initialState,
	reducers: {
		queryPending: (state) => {
			state.isLoading = true;
		},
		querySuccess: (state, { payload }) => {
			state.isLoading = false;
			state.songs = payload;
		},
		queryError: (state, { payload }) => {
			state.isLoading = false;
			state.songs = [];
		},
	},
});

const { reducer, actions } = querySlice;

export const {
	queryPending,
	querySuccess,
	queryError,
} = actions;

export default reducer;