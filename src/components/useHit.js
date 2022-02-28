import axios from "axios";

export const hitURL = "https://stocker-be-api.herokuapp.com";

export default function useHit(path) {
  async function send(params) {
    return await new Promise((r, e) => {
      axios.post(hitURL + path, params).then(
        (res) => {
          r(res.data);
        },
        (err) => {
          e(err.response.data);
        }
      );
    });
  }

  return send;
}
