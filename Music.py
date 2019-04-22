import numpy as np  # To generate random numbers
import tensorflow as tf

#hyperparameters like learning rate 
#rnns
from deepmusic.moduleloader import ModuleLoader
#predicts next key
from deepmusic.keyboardcell import KeyboardCell
#encapsulates song data, can run get scale, get relative note, etc. 
import deepmusic.songstruct as music

def _build_network(self):
    #create the computation graph, encapsulates sessions and graph initialization
    input_dim = ModuleLoader.batch_builders.get_module().get_input_dim()
        
        # A placeholder exists solely to serve as the target of feeds. 
        #It is not initialized and contains no data. A placeholder generates 
        #an error if it is executed without a feed, so you won't forget to feed it.
        #for music data
        with tf.name_scope('placeholder_inputs'):
            self.inputs = [
                tf.placeholder(
                    tf.float32,  # numerical data
                    [self.args.batch_size, input_dim],  #how much data
                    name='input')
                for _ in range(self.args.sample_length) #size of input, 1
                ]
        
        #0 or 1, 88 key binary classification
        with tf.name_scope('placeholder_targets'):
            self.targets = [
                tf.placeholder(
                    tf.int32,  # 0/1 
                    [self.args.batch_size],  
                    name='target')
                for _ in range(self.args.sample_length)
                ]
        
        #uses previous hidden state
        with tf.name_scope('placeholder_use_prev'):
            self.use_prev = [
                tf.placeholder(
                    tf.bool,
                    [],
                    name='use_prev')
                for _ in range(self.args.sample_length)  
                ]

        
        # Define the network
        self.loop_processing = ModuleLoader.loop_processings.build_module(self.args)
        def loop_rnn(prev, i):
            """ Loop function used to connect one output of the rnn to the next input.
            The previous input and returned value have to be from the same shape.
            This is useful to use the same network for both training and testing.
            Args:
                prev: the previous predicted keyboard configuration at step i-1
                i: the current step id (Warning: start at 1, 0 is ignored)
            Return:
                tf.Tensor: the input at the step i
            """
            next_input = self.loop_processing(prev)

            #Tensors returned by the call to either fn1 or fn2. 
            #If the callables return a singleton list, 
            #the element is extracted from the list.
            #conditional
            # On training, we force the correct input, on testing, we use the previous output as next input
            return tf.cond(self.use_prev[i], lambda: next_input, lambda: self.inputs[i])

        
        #built in seq2seq, outputs prediction notes, 
        self.outputs, self.final_state = tf.nn.seq2seq.rnn_decoder(
            decoder_inputs=self.inputs,
            initial_state=None,  # The initial state is defined inside KeyboardCell
            cell=KeyboardCell,
            loop_function=loop_rnn
        )

        # For training only
        if not self.args.test:
            # Finally, we define the loss function

            # The network will predict a mix a wrong and right notes. 
            For the loss function, we would like to
            # penalize note which are wrong. Eventually, the penalty 
            should be less if the network predict the same
            # note but not in the right pitch (ex: C4 instead of C5), 
            with a decay the further the prediction
            # is (D5 and D1 more penalized than D4 and D3 if the target is D2)

          
            
        #minimize error 
            loss_fct = tf.nn.seq2seq.sequence_loss(
                self.outputs,
                self.targets,
                softmax_loss_function=tf.nn.softmax_cross_entropy_with_logits,  
                average_across_timesteps=True,  
                average_across_batch=True
            )
            

            #Initialize the optimizer
            opt = tf.train.AdamOptimizer(
                learning_rate=self.current_learning_rate,
                beta1=0.9,
                beta2=0.999,
                epsilon=1e-08
            )
            self.opt_op = opt.minimize(loss_fct)
