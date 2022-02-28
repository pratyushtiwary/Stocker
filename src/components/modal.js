import { motion, AnimatePresence } from "framer-motion";
import { useEffect } from "react";
import styles from "../styles/components/modal.module.css";

export default function Model({ open, children, onClose }) {
  useEffect(() => {
    if (open) {
      document.body.style.overflowY = "hidden";
    } else {
      document.body.style.overflowY = "auto";
    }
  }, [open]);
  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ scale: 0, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          exit={{ scale: 0, opacity: 0 }}
          className={styles.modal}
        >
          <div className={styles.close}>
            <button className={styles.closeBtn} onClick={onClose}>
              x
            </button>
          </div>
          {children}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
