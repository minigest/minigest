import React from "react";
import { isEmpty } from "lodash";
import {
  Percentuale,
  LoadingSpinner,
  ListaVuota,
  TableCellIcon,
} from "~/Components";
import { makeStyles } from "@material-ui/styles";
import {
  TableContainer,
  Paper,
  Box,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  Typography,
  IconButton,
} from "@material-ui/core";
import EditIcon from "@material-ui/icons/Edit";
import DeleteForeverIcon from "@material-ui/icons/DeleteForever";
import { orange, red } from "@material-ui/core/colors";

const useStyles = makeStyles((theme) => ({
  editButton: {
    color: orange[500],
    "&:hover": {
      color: orange[700],
    },
  },
  deleteButton: {
    color: red[500],
    "&:hover": {
      color: red[700],
    },
  },
}));

export function Lista(props) {
  const classes = useStyles();
  const { results, getting, getError, onEdit, onDelete } = props;

  return getting ? (
    <LoadingSpinner />
  ) : isEmpty(results) ? (
    <ListaVuota message={getError || `Non ci sono tassi da visualizzare`} />
  ) : (
    <Paper>
      {getError && (
        <Box p={2}>
          <Typography gutterBottom color="error">
            {getError}
          </Typography>
        </Box>
      )}

      <TableContainer component={Paper}>
        <Table aria-label="interessi legali">
          <TableHead>
            <TableRow>
              <TableCell>Data</TableCell>
              <TableCell align="right">Percentuale</TableCell>
              <TableCellIcon>
                <EditIcon />
              </TableCellIcon>
              <TableCellIcon>
                <DeleteForeverIcon />
              </TableCellIcon>
            </TableRow>
          </TableHead>

          <TableBody>
            {results.map((tasso) => (
              <TableRow key={tasso.id}>
                <TableCell>{tasso.data}</TableCell>
                <TableCell align="right">
                  <Percentuale value={parseFloat(tasso.percentuale)} />
                </TableCell>
                <TableCellIcon>
                  <IconButton
                    className={classes.editButton}
                    onClick={() => onEdit(tasso)}
                  >
                    <EditIcon color="inherit" />
                  </IconButton>
                </TableCellIcon>
                <TableCellIcon>
                  <IconButton
                    className={classes.deleteButton}
                    onClick={() => onDelete(tasso.id)}
                  >
                    <DeleteForeverIcon color="inherit" />
                  </IconButton>
                </TableCellIcon>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Paper>
  );
}