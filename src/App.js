import Header from "./components/header";
import Input from "./components/input";
import useMaxWidth from "./components/useMaxWidth";
import "./styles/globals.css";
import { useEffect, useState } from "react";
import styles from "./styles/index.module.css";
import hero from "./images/hero.svg";
import one from "./images/1.svg";
import two from "./images/2.svg";
import three from "./images/3.svg";
import useHit from "./components/useHit";
import Modal from "./components/modal";
import Loading from "./components/loading";

function App() {
  const maxWidth = useMaxWidth(762);
  const modalMaxWidth = useMaxWidth(605);
  const sendRequest = useHit("/api/save");
  const [email, setEmail] = useState("");
  const [openModal, setOpenModal] = useState(false);
  const [modalContent, setModalContent] = useState(0);
  const [showLoader, setShowLoader] = useState(false);

  useEffect(() => {
    window.addEventListener("keyup", function (e) {
      if (e.which === 27 || e.keyCode === 27 || e.code === "Escape") {
        setOpenModal(false);
      }
    });
  }, []);

  function saveData() {
    setShowLoader(true);
    sendRequest({
      email: email,
    })
      .then((res) => {
        setShowLoader(false);
        setModalContent(0);
        setOpenModal(true);
      })
      .catch((err) => {
        setShowLoader(false);

        if (err.msg === "Maximum limit reached!") {
          setModalContent(2);
        } else {
          setModalContent(1);
        }
        setOpenModal(true);
      });
  }

  return (
    <>
      <Header />
      <section className={styles.main}>
        {maxWidth && (
          <div className={styles.hero}>
            <img
              src={hero}
              alt="Illustration representing message sending"
              className={styles.img}
            />
          </div>
        )}
        <div className={styles.container}>
          <h2 className={styles.heading}>
            Get <u>NSE</u> and <u>BSE</u> Announcements at your fingertips
          </h2>
          <Input
            type="email"
            label="Enter your email"
            actionText=">"
            id="email"
            required
            className={styles.input}
            onSubmit={saveData}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        {!maxWidth && (
          <div className={styles.hero}>
            <img
              src={hero}
              alt="Illustration representing message sending"
              className={styles.img}
            />
          </div>
        )}
      </section>
      <section className={styles.howItWorksSection}>
        <div className={styles.wave}></div>
        <h2 className={styles.heading}>
          How It <u>Works</u>?
        </h2>
        <div className={styles.content}>
          <div className={styles.item + " " + styles.left}>
            <div className={styles.infoGraphic}>
              <img src={one} alt="Illustration representing saving documents" />
            </div>
            <p className={styles.desc}>
              We take your email and <u>securely</u> save it with us
            </p>
          </div>
          <div className={styles.item + " " + styles.right}>
            {maxWidth && (
              <div className={styles.infoGraphic}>
                <img
                  src={two}
                  alt="Illustration showing a man looking at content of a website"
                />
              </div>
            )}
            <p className={styles.desc}>
              We check <u>NSE</u> ans <u>BSE</u> website everyday and create a
              report for you
            </p>
            {!maxWidth && (
              <div className={styles.infoGraphic}>
                <img
                  src={two}
                  alt="Illustration showing a man looking at content of a website"
                />
              </div>
            )}
          </div>
          <div className={styles.item + " " + styles.left}>
            <div className={styles.infoGraphic}>
              <img
                src={three}
                alt="Illustration representing sending a message"
              />
            </div>
            <p className={styles.desc}>
              Then we send that report to your <u>email</u>
            </p>
          </div>
        </div>
      </section>
      <Modal open={openModal} onClose={() => setOpenModal(false)}>
        {modalContent === 0 && (
          <div className={styles.success}>
            {modalMaxWidth && (
              <div className={styles.img}>
                <img src="/success.svg" alt="We've saved your email" />
              </div>
            )}
            <div className={styles.content}>
              <h2>Success!</h2>
              <p>
                Yay! We have saved your email and will send you a report every
                day
              </p>
            </div>
            {!modalMaxWidth && (
              <div className={styles.img}>
                <img src="/success.svg" alt="We've saved your email" />
              </div>
            )}
          </div>
        )}
        {modalContent === 1 && (
          <div className={styles.error}>
            {modalMaxWidth && (
              <div className={styles.img}>
                <img src="/exists.svg" alt="Email already exists" />
              </div>
            )}
            <div className={styles.content}>
              <h2>Whoops!</h2>
              <p>Looks like you are already there in our database.</p>
            </div>
            {!modalMaxWidth && (
              <div className={styles.img}>
                <img src="/exists.svg" alt="Email already exists" />
              </div>
            )}
          </div>
        )}
        {modalContent === 2 && (
          <div className={styles.error}>
            {modalMaxWidth && (
              <div className={styles.img}>
                <img src="/full.svg" alt="Maximum limit reached" />
              </div>
            )}
            <div className={styles.content}>
              <h2>Whoops!</h2>
              <p>
                Looks like we have reached our limit of emails. :(
                <br /> Try registering after a year of so. Sorry :( day
              </p>
            </div>
            {!modalMaxWidth && (
              <div className={styles.img}>
                <img src="/full.svg" alt="Maximum limit reached" />
              </div>
            )}
          </div>
        )}
      </Modal>
      <Loading open={showLoader} />
    </>
  );
}

export default App;
